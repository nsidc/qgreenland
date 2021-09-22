from pathlib import Path

from qgreenland.util.config.compile import compile_cfg


# Figure out the config dir locally to avoid importing anything unnecessary
THIS_DIR = Path(__file__).resolve().parent
CONFIG_DIR = THIS_DIR.parent.parent / 'config'
CONFIG = compile_cfg(CONFIG_DIR.resolve())
