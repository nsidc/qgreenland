"""Exports layer configuration as a CSV file."""

# Hack to import from qgreenland
import os
import sys
from pathlib import Path

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.insert(0, PARENT_DIR)

if __name__ == "__main__":
    from qgreenland.util.config.config import get_config, init_config
    from qgreenland.util.config.export import export_config_csv

    init_config()
    export_config_csv(
        get_config(),
        output_path=Path("./layers.csv"),
        # TODO: Come back to me
        package_name="core",
    )
