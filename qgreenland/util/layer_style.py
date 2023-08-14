from pathlib import Path

from qgreenland.constants.paths import ANCILLARY_DIR


def get_style_filepath(style_name: str) -> Path:
    """Generate a Path object for style file represented by `style_name`."""
    return ANCILLARY_DIR / "styles" / (style_name + ".qml")
