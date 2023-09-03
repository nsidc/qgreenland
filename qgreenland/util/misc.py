from collections import Counter
from collections.abc import Iterator
from pathlib import Path

from qgreenland.constants.paths import COMPILE_PACKAGE_DIR


def find_duplicates(items: Iterator[str]) -> list[str]:
    return [i for i, count in Counter(items).items() if count > 1]


def compile_package_dir(package_name: str) -> Path:
    return COMPILE_PACKAGE_DIR / package_name
