"""Exports layer configuration as a CSV file."""

# Hack to import from qgreenland
import os, sys  # noqa: E401
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.insert(0, PARENT_DIR)


from qgreenland.config import CONFIG  # noqa: E402
from qgreenland.util.config import export_config_csv  # noqa: E402

if __name__ == '__main__':
    export_config_csv(CONFIG)
