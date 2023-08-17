import datetime as dt
import logging
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape

import anytree
import qgis.core as qgc
from PyQt5.QtGui import QColor

from qgreenland import exceptions as exc
from qgreenland.constants.project import PROJECT
from qgreenland.models.config.layer_group import LayerGroupSettings
from qgreenland.util.config.config import get_config
from qgreenland.util.qgis.layer import make_map_layer
from qgreenland.util.tree import LayerGroupNode, LayerNode, prune_layers_not_in_package
from qgreenland.util.version import get_build_version

logger = logging.getLogger("luigi-interface")


class QgsApplicationContext:
    """Context manager for setting up and tearing down the QgsApplication.

    WARNING: This context manager should be used once and only once per program
    execution. Attempting to use this context manager more than once may cause a
    segfault.
    """

    def __enter__(self):
        self.qgs = _setup_qgs_app()

        return self.qgs

    def __exit__(self, _exc_type, _exc_value, _traceback):
        # Run `exitQgis` to properly cleanup the QgsApplication. Not doing so
        # causes a segfault on program completion.
        self.qgs.exitQgis()


def make_qgis_project_file(path: Path) -> None:
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs/.qgz project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    config = get_config()

    # Create a new project; initializes basic structure
    project = qgc.QgsProject.instance()
    project.write(str(path))

    project_crs = qgc.QgsCoordinateReferenceSystem(config.project.crs)
    project.setCrs(project_crs)

    # Set the map background color to be gray (same color as Quantarctica)
    project.setBackgroundColor(QColor(200, 200, 200))

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()

    project_rectangle = qgc.QgsReferencedRectangle(
        qgc.QgsRectangle(
            config.project.boundaries["data"].bbox.min_x,
            config.project.boundaries["data"].bbox.min_y,
            config.project.boundaries["data"].bbox.max_x,
            config.project.boundaries["data"].bbox.max_y,
        ),
        project_crs,
    )
    view.setDefaultViewExtent(project_rectangle)

    _add_decorations(project)

    package_layer_tree = prune_layers_not_in_package(config.layer_tree)
    _add_layers_and_groups(project, package_layer_tree)

    _add_project_metadata(project)

    # TODO: is it normal to write multiple times?
    project.write()

    # Release all file locks! If we don't do this, we won't be able to clean up
    # layer source files after zipping the project.
    project.clear()


def _add_project_metadata(project: qgc.QgsProject) -> None:
    """Add project-level metadata (title, authors, abstract).

    This information is viewable in the **Project > Properties** in QGIS.
    """
    project_metadata = project.metadata()
    project_metadata.setAuthor("QGreenland team")
    project_metadata.setTitle(PROJECT)
    project_metadata.setAbstract(
        """QGreenland is a free and open-source Greenland-focused GIS package
for QGIS. To learn more about QGreenland, visit our website:
https://qgreenland.org.

For information on how to cite QGreenland, please see:
https://qgreenland.readthedocs.io/en/latest/citing.html"""
    )
    project.setMetadata(project_metadata)


def _apply_group_settings(
    group: qgc.QgsLayerTreeGroup,
    settings: LayerGroupSettings,
) -> None:
    group.setItemVisibilityChecked(settings.show)
    group.setExpanded(settings.expand)


def _add_layers_and_groups(project: qgc.QgsProject, layer_tree: LayerGroupNode) -> None:
    """Iterate through the layer tree and create the relevant Qgs objects."""
    # `anytree.PreOrderIter` is necessary here so that the
    # `_create_and_add_layer` function receives the correct group.
    for node in anytree.PreOrderIter(
        layer_tree,
        filter_=lambda node: not node.is_root,
    ):
        if type(node) is LayerGroupNode:
            _get_or_create_and_configure_group(
                node=node,
                project=project,
            )
        elif type(node) is LayerNode:
            # The parent group should already exist because `preOrderIter` will
            # return `LayerGroupNode`s first.
            parent_group = _get_group(
                project=project,
                group_path=node.group_name_path,
            )
            _create_and_add_layer(
                node=node,
                project=project,
                group=parent_group,
            )
        else:
            raise TypeError(f"Unexpected `node` type: {type(node)}")

    logger.debug("Done adding layers.")


def _get_group(
    *,
    project: qgc.QgsProject,
    group_path: tuple[str, ...],
) -> qgc.QgsLayerTreeGroup:
    # Starting at the root of the layer tree, climb the tree until we reach the
    # parent of group_node.
    group = project.layerTreeRoot()
    for group_name in group_path:
        group = group.findGroup(group_name)
        if not group:
            raise exc.QgrQgsLayerTreeGroupError(
                f"Unable to find group {group_path}.",
            )

    return group


def _get_or_create_and_configure_group(
    *,
    node: LayerGroupNode,
    project: qgc.QgsProject,
) -> qgc.QgsLayerTreeGroup:
    group_path = node.group_name_path
    try:
        parent_group = _get_group(
            project=project,
            group_path=group_path,
        )
    except exc.QgrQgsLayerTreeGroupError as e:
        raise exc.QgrQgsLayerTreeGroupError(
            f"Parent group of {node.name} not found: {e}",
        )

    new_group = parent_group.addGroup(node.name)

    # Update settings from the settings object
    if type(node.settings) is LayerGroupSettings:
        _apply_group_settings(new_group, node.settings)

    return new_group


def _create_and_add_layer(
    *,
    node: LayerNode,
    project: qgc.QgsProject,
    group: qgc.QgsLayerTreeGroup,
) -> None:
    layer_id = node.name
    logger.debug(f"Adding {layer_id}...")
    layer_cfg = node.layer_cfg

    map_layer = make_map_layer(node)

    # Assign to a different name because this changes the type. We need to add
    # `map_layer` to the project as the last step.
    grouped_layer = group.addLayer(map_layer)
    grouped_layer.setItemVisibilityChecked(
        layer_cfg.show,
    )

    # All layers start collapsed. When expanded (the default), they show the
    # entire colormap. This takes up a large amount of space in the QGIS table
    # of contents.
    grouped_layer.setExpanded(False)

    project.addMapLayer(map_layer, addToLegend=False)


def _get_qgs_prefix_path() -> Path:
    # The qgis prefix path is two directories above the qgis executable.
    # See:
    # https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    qgis_path = (
        subprocess.run(
            ["which", "qgis"],
            stdout=subprocess.PIPE,
        )
        .stdout.decode("utf-8")
        .strip("\n")
    )
    qgis_prefix_path = (Path(qgis_path) / ".." / "..").resolve()

    return qgis_prefix_path


def _setup_qgs_app() -> qgc.QgsApplication:
    """Set up QgsApplication.

    This function should only be called once to instantiate a
    QgsApplication. Once all pyqgis operations are complete, the QgsApplication
    MUST be cleaned up with the QgsApplication instance's `exitQgis`
    method. Failure to do so will result in a segmentation fault.
    """
    qgis_prefix_path = _get_qgs_prefix_path()

    # Boilerplate QGIS initialization code;
    # - Suppresses "Application path not intialized" errors
    # - Enables Qt support for fonts used in layer styles (labels)
    qgs = qgc.QgsApplication([], False)
    qgs.initQgis()
    qgc.QgsApplication.setPrefixPath(str(qgis_prefix_path), True)

    return qgs


def _add_decorations(project: qgc.QgsProject) -> None:
    """Add "decorations" to QGIS project.

    Decorations are overlaid on the QGIS viewport.
    """
    logger.debug("Adding decorations...")
    # Add CopyrightLabel:
    project.writeEntry("CopyrightLabel", "/Enabled", True)
    # project.writeEntry('CopyrightLabel', '/FontName', 'Sans Serif')
    # NOTE: Does the copyright symbol work this way or should we use HTML codes?
    year = dt.date.today().year
    copyright_label = escape(
        f"QGreenland {get_build_version()} © NSIDC {year}"
        "\nhttps://qgreenland.org | https://github.com/nsidc/qgreenland/",
    )
    project.writeEntry("CopyrightLabel", "/Label", copyright_label)
    project.writeEntry("CopyrightLabel", "/Placement", 0)
    project.writeEntry("CopyrightLabel", "/MarginH", 0)
    project.writeEntry("CopyrightLabel", "/MarginV", 0)

    # TODO: can we figure out a way to export `text_format` to xml so that it
    # can be written to the project file without hard-coding everything? The
    # `text_format` (`QgsTextFormat`) object has a `writeXml` method but it is
    # unclear how to apply it to the project file.

    # text_format = qgc.QgsTextFormat()
    # buffer_settings = text_format.buffer()
    # buffer_settings.setEnabled(True)
    # text_format.setBuffer(buffer_settings)

    project.writeEntry(
        "CopyrightLabel",
        "/Font",
        """<text-style multilineHeightUnit="Percentage" forcedItalic="0" namedStyle="Regular" forcedBold="0" capitalization="0" fontWeight="50" fontKerning="1" fontItalic="0" fontStrikeout="0" blendMode="0" fontWordSpacing="0" multilineHeight="1" fontSizeUnit="Point" textOrientation="horizontal" textColor="50,50,50,255" textOpacity="1" fontSize="10" fontSizeMapUnitScale="3x:0,0,0,0,0,0" previewBkgrdColor="255,255,255,255" allowHtml="0" fontFamily="Open Sans" fontLetterSpacing="0" fontUnderline="0">
 <families/>
 <text-buffer bufferColor="250,250,250,255" bufferJoinStyle="128" bufferSize="1" bufferDraw="1" bufferSizeUnits="MM" bufferOpacity="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1"/>
 <text-mask maskEnabled="0" maskOpacity="1" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskType="0" maskSize="0" maskSizeUnits="MM" maskedSymbolLayers="" maskJoinStyle="128"/>
 <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="Point" shapeType="0" shapeDraw="0" shapeBlendMode="0" shapeSizeX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="Point" shapeOpacity="1" shapeRadiiX="0" shapeSizeType="0" shapeOffsetX="0" shapeRadiiUnit="Point" shapeRadiiY="0" shapeSVGFile="" shapeFillColor="255,255,255,255" shapeOffsetY="0" shapeOffsetUnit="Point" shapeRotationType="0" shapeRotation="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0">
  <symbol force_rhr="0" clip_to_extent="1" is_animated="0" frame_rate="10" alpha="1" type="marker" name="markerSymbol">
   <data_defined_properties>
    <Option type="Map">
     <Option type="QString" name="name" value=""/>
     <Option name="properties"/>
     <Option type="QString" name="type" value="collection"/>
    </Option>
   </data_defined_properties>
   <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
    <Option type="Map">
     <Option type="QString" name="angle" value="0"/>
     <Option type="QString" name="cap_style" value="square"/>
     <Option type="QString" name="color" value="190,178,151,255"/>
     <Option type="QString" name="horizontal_anchor_point" value="1"/>
     <Option type="QString" name="joinstyle" value="bevel"/>
     <Option type="QString" name="name" value="circle"/>
     <Option type="QString" name="offset" value="0,0"/>
     <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
     <Option type="QString" name="offset_unit" value="MM"/>
     <Option type="QString" name="outline_color" value="35,35,35,255"/>
     <Option type="QString" name="outline_style" value="solid"/>
     <Option type="QString" name="outline_width" value="0"/>
     <Option type="QString" name="outline_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
     <Option type="QString" name="outline_width_unit" value="MM"/>
     <Option type="QString" name="scale_method" value="diameter"/>
     <Option type="QString" name="size" value="2"/>
     <Option type="QString" name="size_map_unit_scale" value="3x:0,0,0,0,0,0"/>
     <Option type="QString" name="size_unit" value="MM"/>
     <Option type="QString" name="vertical_anchor_point" value="1"/>
    </Option>
    <data_defined_properties>
     <Option type="Map">
      <Option type="QString" name="name" value=""/>
      <Option name="properties"/>
      <Option type="QString" name="type" value="collection"/>
     </Option>
    </data_defined_properties>
   </layer>
  </symbol>
  <symbol force_rhr="0" clip_to_extent="1" is_animated="0" frame_rate="10" alpha="1" type="fill" name="fillSymbol">
   <data_defined_properties>
    <Option type="Map">
     <Option type="QString" name="name" value=""/>
     <Option name="properties"/>
     <Option type="QString" name="type" value="collection"/>
    </Option>
   </data_defined_properties>
   <layer class="SimpleFill" pass="0" locked="0" enabled="1">
    <Option type="Map">
     <Option type="QString" name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
     <Option type="QString" name="color" value="255,255,255,255"/>
     <Option type="QString" name="joinstyle" value="bevel"/>
     <Option type="QString" name="offset" value="0,0"/>
     <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
     <Option type="QString" name="offset_unit" value="MM"/>
     <Option type="QString" name="outline_color" value="128,128,128,255"/>
     <Option type="QString" name="outline_style" value="no"/>
     <Option type="QString" name="outline_width" value="0"/>
     <Option type="QString" name="outline_width_unit" value="Point"/>
     <Option type="QString" name="style" value="solid"/>
    </Option>
    <data_defined_properties>
     <Option type="Map">
      <Option type="QString" name="name" value=""/>
      <Option name="properties"/>
      <Option type="QString" name="type" value="collection"/>
     </Option>
    </data_defined_properties>
   </layer>
  </symbol>
 </background>
 <shadow shadowUnder="0" shadowScale="100" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOpacity="0.69999999999999996" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowRadius="1.5" shadowOffsetDist="1" shadowOffsetGlobal="1" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowBlendMode="6"/>
 <dd_properties>
  <Option type="Map">
   <Option type="QString" name="name" value=""/>
   <Option name="properties"/>
   <Option type="QString" name="type" value="collection"/>
  </Option>
 </dd_properties>
</text-style>""",
    )

    # Add Image (QGreenland logo):
    project.writeEntry("Image", "/Enabled", True)
    project.writeEntry("Image", "/Placement", 0)
    project.writeEntry("Image", "/MarginH", 4)
    project.writeEntry("Image", "/MarginV", 8)
    project.writeEntry("Image", "/Size", 24)
    project.writeEntry("Image", "/ImagePath", "qgreenland.png")

    # Enable the scalebar
    project.writeEntry("ScaleBar", "/Enabled", True)
    # Placement 3 corresponds to lower-right corner
    project.writeEntry("ScaleBar", "/Placement", 3)

    logger.debug("Done adding decorations.")
