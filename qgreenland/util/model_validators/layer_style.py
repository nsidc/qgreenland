from xml.etree import ElementTree

import qgreenland.exceptions as exc
from qgreenland.util.layer_style import get_style_filepath


def validate_style_file_exists(style_name: str):
    """Ensure the QML style file exists in the configuration."""
    if style_name:
        style_filepath = get_style_filepath(style_name)
        if not style_filepath.is_file():
            raise exc.QgrInvalidConfigError(
                f"Style file does not exist: {style_filepath}"
            )

    return style_name


def validate_style_file_only_contains_allowed_fonts(style_name: str):
    """Ensure only fonts that can be downloaded by QGIS are in our style files.

    This ensures we don't re-trigger an old issue:
        https://github.com/nsidc/qgreenland/issues/515
    """
    # TODO: Is the full list of supported fonts available in PyQGIS' API? I think
    # this is the complete list, but haven't found it in the Python API yet:
    #     https://github.com/qgis/QGIS/blob/a7b31c7db29328fc44966a854d22c452f58c77c1/src/core/textrenderer/qgsfontmanager.cpp#L203-L925
    allowed_fonts = ["Open Sans"]
    if style_name:
        style_filepath = get_style_filepath(style_name)
        tree = ElementTree.parse(style_filepath)

        # Check every XML tag for a `fontFamily` attribute with an undesired value
        for elem in tree.getroot().iter():
            if font_family := elem.attrib.get("fontFamily", False):
                if font_family not in allowed_fonts:
                    raise exc.QgrInvalidConfigError(
                        f"Style {style_filepath} contains disallowed font:"
                        f" '{font_family}'."
                        f" Only the following fonts are allowed: {allowed_fonts}."
                    )

    return style_name


def validate_style_file_unit_suffixes(style_name: str):
    """Ensure common errors in style configuration of unit suffixes are avoided.

    For example, the "Label unit suffix" field in the QGIS Layer Symbology menu seems
    like the only place to populate this data, but if the displayed color ramp legend is
    continuous (new feature in 3.18), then the "suffix" field in the "Legend Settings"
    menu will be used. If the former is populated, ensure the latter matches.

    Also ensures that continuous legends are horizontal.
    """
    error_prefix = (
        f"Style '{style_name}' has a continuous legend that is incorrectly"
        f" configured:"
    )

    if style_name:
        style_filepath = get_style_filepath(style_name)
        tree = ElementTree.parse(style_filepath)

        colorrampshader = tree.find(".//colorrampshader")
        if colorrampshader is None:
            # This style is not using a colorramp, so there is no "Label unit suffix"
            # setting to be concerned with.
            return style_name

        if colorrampshader.attrib["classificationMode"] != "1":
            # This colorramp is not continuous, so the  "Label unit suffix" will be
            # used if specified.
            return style_name

        first_item = colorrampshader.find(".//item")

        if first_item is None:
            # Color ramp is empty anyway... should this be a validation error?
            return style_name

        unit_suffix = first_item.attrib["label"].removeprefix(
            first_item.attrib["value"]
        )

        if not unit_suffix:
            # The first colorrampitem's label does not contain a suffix set by the
            # "Label unit suffix" field in QGIS. We can assume the style is set up as
            # the user intended.
            return style_name

        rampLegendSettings = colorrampshader.find(".//rampLegendSettings")
        continuous_legend_suffix = (
            rampLegendSettings.attrib["suffix"] if rampLegendSettings else None
        )

        if continuous_legend_suffix == unit_suffix:
            if rampLegendSettings and rampLegendSettings.attrib["orientation"] != "1":
                raise exc.QgrInvalidConfigError(
                    f"{error_prefix}\n"
                    "    Continuous legend orientation must be horizontal.\n"
                    f"In QGIS >=3.28, edit this style ({style_filepath}) in"
                    " the layer symbology menu and set the orientation in the"
                    ' "Legend Settings" menu.'
                )

            # This style's suffixes and orientation are set up correctly!
            return style_name

        raise exc.QgrInvalidConfigError(
            f"{error_prefix}\n"
            f"    {continuous_legend_suffix=} != {unit_suffix=}\n"
            f"In QGIS >=3.28, edit this style ({style_filepath}) in the layer symbology"
            ' menu and ensure that the "Label unit suffix" exactly matches the "suffix"'
            ' field in the "Legend Settings" menu.'
        )
