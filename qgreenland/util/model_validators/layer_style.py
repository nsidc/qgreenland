from xml.etree import ElementTree

from qgis.core import QgsRendererRangeLabelFormat

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

        first_value = first_item.attrib["value"]
        first_label = first_item.attrib["label"]

        label_precision = int(colorrampshader.attrib.get("labelPrecision", "0"))
        unit_suffix = _get_unit_suffix(
            value=first_value,
            label=first_label,
            label_precision=label_precision,
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

        # QGIS can be really finicky with the "Label unit suffix" field because its
        # value is not saved into the XML as a dedicated field like one would expect.
        # Instead, the labels are pre-calculated to add prefixes and suffixes, then
        # saved in whole to the XML. This means that for QGIS to display a "Label unit
        # suffix" field in the GUI, it has to calculate the suffixes and prefixes from
        # the labels in the XML. Strange errors can be introduced during this process,
        # like seemingly-random numbers being prepended to the "Label unit suffix" value
        # in the GUI, and then propagating to all labels in the XML.
        raise exc.QgrInvalidConfigError(
            f"{error_prefix}\n"
            f"    {continuous_legend_suffix=} != {unit_suffix=}\n"
            f"In QGIS >=3.28, edit this style ({style_filepath}) in the layer symbology"
            ' menu and ensure that the "Label unit suffix" exactly matches the "suffix"'
            ' field in the "Legend Settings" menu. If the suffixes reported in this'
            ' error message look wrong to you, you may need to re-check the "Label unit'
            ' suffix" and press the "Classify"  button and re-save the style to correct'
            " errors."
        )


def _get_unit_suffix(*, label: str, value: str, label_precision: int = 0) -> str | None:
    """Calculate the unit suffix for a QGIS colormap entry.

    A QGIS style's `<colorrampshader>` has a `labelPrecision` attribute. Each `<item>`
    within has a `label` and a `value` attribute. In order to calculate the suffix from
    the `label`, we need to calculate the non-suffix part of the `label` based on
    `value`.  Then we can difference the calculated label (sans suffix) and the real
    label to get the suffix.

    TODO: Support a "clip" argument (originates in `<colorrampshader>` element)? Not
    sure how that's set in the GUI but seems to usually be 0.

    TODO: Does not support large numbers well, adds commas where the QGIS symbology menu
    does not.
            formatter.formatNumber(float(-9902))
            >>> '-9,902'
    """
    formatter = QgsRendererRangeLabelFormat()
    formatter.setTrimTrailingZeroes(False)  # Does this setting correspond with "clip"?
    formatter.setPrecision(label_precision)

    formatted_value = formatter.formatNumber(float(value))
    return label.removeprefix(formatted_value)
