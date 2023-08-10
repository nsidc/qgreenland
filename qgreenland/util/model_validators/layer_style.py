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


def validate_style_file_continuous_legend(style_name: str):
    """Ensure common errors in continuous legend configuration are avoided.

    * Ensures continuous legend is enabled for "linear" interpolated colorramps.
    * Ensures continuous legends are horizontal.
    * Ensures a "Suffix" is populated in the "Legend Settings" menu.
    """
    if not style_name:
        return style_name

    style_filepath = get_style_filepath(style_name)
    tree = ElementTree.parse(style_filepath)

    errors = []
    error_prefix = (
        f"Style '{style_name}' has a continuous legend that is incorrectly"
        " configured."
        f" In QGIS >=3.28, edit this style ({style_filepath}) in the layer symbology"
        ' menu and configure the continuous legend in the "Legend Settings" submenu to'
        " resolve the following:"
    )
    error_suffix = (
        "Please see our documentation:"
        " <https://qgreenland.readthedocs.io/en/latest/contributor/how-to"
        "/contribute-styles.html#continuous-colormap-considerations>"
    )

    colorrampshader = tree.find(".//colorrampshader")
    if colorrampshader is None:
        # This style is not using a colorramp, so there is no "Label unit suffix"
        # setting to be concerned with.
        return style_name

    if colorrampshader.attrib["colorRampType"] != "INTERPOLATED":
        # This colorramp should not have a continuous legend, so the  "Label unit
        # suffix" will be used if specified.
        return style_name

    rampLegendSettings = colorrampshader.find(".//rampLegendSettings")
    if not rampLegendSettings:
        raise exc.QgrInvalidConfigError(
            f"{error_prefix}\n"
            "  * Continuous (i.e. linearly interpolated) colorramps must be"
            " re-configured with a newer version of QGIS to support continuous legends."
            ' Please ensure that the unit of measurement is populated in the "Suffix"'
            ' field, and that the "Orientation" field is set to "Horizontal".\n'
            f"{error_suffix}"
        )

    if (orientation := rampLegendSettings.attrib["orientation"]) != "1":
        errors.append(
            f'"Orientation" must be horizontal ("1"). Is currently "{orientation}"'
        )

    if not (suffix := rampLegendSettings.attrib["suffix"]):
        # Populating " " is a workaround for the rare case a layer with a continuous
        # legend has no unit of measurement. Validating the Suffix matches the
        # "Layer unit suffix" may be a more thorough check, but it's much more
        # difficult because QGIS doesn't store "Layer unit suffix" in any particular
        # field. It's calculated on-the-fly in an unreliable way, depending on QGIS
        # version.
        errors.append(
            f'"Suffix" must contain a unit of measurement. Is currently "{suffix}".'
            " If this layer truly has no unit of measurement (e.g. NDVI or a count),"
            ' populate a space (" ") to silence this error'
        )

    if errors:
        # NOTE: chr(92) is a backslash to work around "f-string expression part
        # cannot include a backslash" and still put a newline in there.
        newline = "\n"
        raise exc.QgrInvalidConfigError(
            f"{error_prefix}\n"
            f"{newline.join(f'  * {err}' for err in errors)}\n"
            f"{error_suffix}"
        )

    return style_name
