from pathlib import Path

import qgreenland.exceptions as exc


def get_layer_fp(layer_dir: Path) -> Path:
    """Look for one and only one standard file type 'gpkg' or 'tif'."""
    # TODO: Extract standard file types into some structure
    rasters = list(layer_dir.glob("*.tif"))
    vectors = list(layer_dir.glob("*.gpkg"))
    files = rasters + vectors

    if len(files) != 1:
        raise exc.QgrRuntimeError(
            "Expected exactly 1 .tif or .gpkg in layer output directory"
            f" {layer_dir}. Found: {files}.",
        )

    return files[0]


def directory_contents(dir_path: Path) -> list[Path]:
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise exc.QgrRuntimeError(f"`dir_path` must be a directory. Got {dir_path}")

    return sorted(
        dir_path.glob("**/*"),
    )


def directory_size_bytes(dir_path: Path) -> int:
    """Return the size of the directory's contents in bytes."""
    contents = directory_contents(dir_path)
    total_size = 0
    for content in contents:
        total_size += content.stat().st_size

    return total_size
