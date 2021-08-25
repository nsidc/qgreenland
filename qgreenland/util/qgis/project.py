import datetime as dt
import logging
import os
import subprocess
from typing import List, Optional
from xml.sax.saxutils import escape

import anytree
import qgis.core as qgc
from PyQt5.QtGui import QColor

from qgreenland.config import CONFIG
from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.layer_group import LayerGroupSettings
from qgreenland.util.qgis.layer import make_map_layer
from qgreenland.util.tree import LayerNode, LayerGroupNode
from qgreenland.util.version import get_build_version

logger = logging.getLogger('luigi-interface')


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


# TODO: make this path a Path
def make_qgis_project_file(path: str) -> None:
    """Create a QGIS project file with the correct stuff in it.

    path: the desired path to .qgs project file, e.g.:
          /luigi/data/qgreenland/qgreenland.qgs

    Developed from examples:

        https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    """
    # Create a new project; initializes basic structure
    project = qgc.QgsProject.instance()
    project.write(path)

    project_crs = qgc.QgsCoordinateReferenceSystem(CONFIG.project.crs)
    project.setCrs(project_crs)

    # Set the map background color to be gray (same color as Quantarctica)
    project.setBackgroundColor(QColor(200, 200, 200))

    # Set the default extent. Eventually we may want to pull the extent directly
    # from the configured 'map frame' layer.
    view = project.viewSettings()

    project_rectangle = qgc.QgsReferencedRectangle(
        qgc.QgsRectangle(
            CONFIG.project.boundaries['data'].bbox.min_x,
            CONFIG.project.boundaries['data'].bbox.min_y,
            CONFIG.project.boundaries['data'].bbox.max_x,
            CONFIG.project.boundaries['data'].bbox.max_y,
        ),
        project_crs,
    )
    view.setDefaultViewExtent(project_rectangle)

    _add_decorations(project)

    _add_layers_and_groups(project, CONFIG.layer_tree)

    # TODO: is it normal to write multiple times?
    project.write()

    # Release all file locks! If we don't do this, we won't be able to clean up
    # layer source files after zipping the project.
    project.clear()


def _set_group_visibility(group: qgc.QgsLayerTreeGroup, visibility: bool) -> None:
    group.setItemVisibilityChecked(visibility)


def _set_group_expanded(group: qgc.QgsLayerTreeGroup, expanded: bool) -> None:
    group.setExpanded(expanded)


def _get_group(
    project: qgc.QgsProject,
    group_path: List[str],
) -> Optional[qgc.QgsLayerTreeGroup]:
    """Find a group in `project` from ordered list of group names.

    e.g. group_path: `['parent', 'child', 'grandchild']`
    """
    group = project.layerTreeRoot()

    # If the group path is an empty string, return the root layer group
    if not group_path:
        return group

    for group_name in group_path:
        group = group.findGroup(group_name)

        # Group not found
        if group is None:
            # TODO: Raise instead of return None?
            return None

    return group


def _add_layers_and_groups(project: qgc.QgsProject, layer_tree: LayerGroupNode) -> None:
    """Iterate through the layer tree and create the relevant Qgs objects."""

    # `anytree.PreOrderIter` is necessary here so that the `_create_and_add_layer`
    # function receives the correct group.
    for node in anytree.PreOrderIter(
            layer_tree,
            filter_=lambda node: not node.is_root,
    ):
        if type(node) is LayerGroupNode:
            current_group = _create_and_configure_group(
                node=node,
                project=project,
            )
        elif type(node) is LayerNode:
            _create_and_add_layer(
                node=node,
                project=project,
                group=current_group,
            )
        else:
            raise TypeError('Unexpected `node` type: {type(node)}')

    logger.debug('Done adding layers.')


def _create_and_configure_group(*, node: LayerGroupNode, project: qgc.QgsProject) -> None:
    group_path = node.group_name_path

    # Starting at the root of the layer tree, climb the tree until we reach the
    # parent of group_node.
    group = project.layerTreeRoot()
    for group_name in group_path:
        group = group.findGroup(group_name)
        if not group:
            raise RuntimeError(
                'Parent group of {node.name} not found: {group_path}'
            )

    group = group.addGroup(node.name)

    # Update settings from the settings object
    if type(node.settings) is LayerGroupSettings:
        _set_group_visibility(group, node.settings.show)
        _set_group_expanded(group, node.settings.expanded)

    return group


def _create_and_add_layer(
        *,
        node: LayerNode,
        project: qgc.QgsProject,
        group: qgc.QgsLayerTreeGroup
) -> None:
    layer_id = node.name
    logger.debug(f'Adding {layer_id}...')
    layer_cfg = node.layer_cfg

    # Remove the root node (named "layers" after the "layers" directory) and
    # remove the layer id

    map_layer = make_map_layer(node)

    # TODO: Why do we have a separate object here?
    grouped_layer = group.addLayer(map_layer)

    # Make the layer invisible and collapsed by default
    grouped_layer.setItemVisibilityChecked(
        layer_cfg.show,
    )

    # All layers start collapsed. When expanded (the default), they show the
    # entire colormap. This takes up a large amount of space in the table of
    # contents.
    grouped_layer.setExpanded(False)

    # TODO: necessary for root group?
    project.addMapLayer(map_layer, addToLegend=False)


def _get_qgs_prefix_path() -> str:
    # The qgis prefix path is two directories above the qgis executable.
    # See:
    # https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
    qgis_path = subprocess.run(
        ['which', 'qgis'],
        stdout=subprocess.PIPE,
    ).stdout.decode('utf-8').strip('\n')
    qgis_prefix_path = os.path.abspath(os.path.join(qgis_path, '..', '..'))

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
    qgc.QgsApplication.setPrefixPath(qgis_prefix_path, True)

    return qgs


def _add_decorations(project: qgc.QgsProject) -> None:
    """Add "decorations" to QGIS project.

    Decorations are overlaid on the QGIS viewport.
    """
    logger.debug('Adding decorations...')
    # Add CopyrightLabel:
    project.writeEntry('CopyrightLabel', '/Enabled', True)
    # project.writeEntry('CopyrightLabel', '/FontName', 'Sans Serif')
    # NOTE: Does the copyright symbol work this way or should we use HTML codes?
    year = dt.date.today().year
    copyright_label = escape(
        f'QGreenland {get_build_version()} © NSIDC {year}'
        '\nhttps://qgreenland.org | https://github.com/nsidc/qgreenland/',
    )
    project.writeEntry('CopyrightLabel', '/Label', copyright_label)
    project.writeEntry('CopyrightLabel', '/Placement', 0)
    project.writeEntry('CopyrightLabel', '/MarginH', 0)
    project.writeEntry('CopyrightLabel', '/MarginV', 0)

    # Add Image (QGreenland logo):
    project.writeEntry('Image', '/Enabled', True)
    project.writeEntry('Image', '/Placement', 0)
    project.writeEntry('Image', '/MarginH', 4)
    project.writeEntry('Image', '/MarginV', 8)
    project.writeEntry('Image', '/Size', 24)
    project.writeEntry('Image', '/ImagePath', 'qgreenland.png')

    logger.debug('Done adding decorations.')
