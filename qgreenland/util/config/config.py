import logging
from functools import cache
from pathlib import Path
from typing import Optional

from qgreenland import exceptions as exc
from qgreenland.models.config import Config
from qgreenland.util.config.compile import compile_cfg

logger = logging.getLogger('luigi-interface')

# Figure out the config dir locally to avoid importing anything unnecessary
THIS_DIR = Path(__file__).resolve().parent
CONFIG_DIR = THIS_DIR.parent.parent / 'config'
_CONFIG: Optional[Config] = None


def init_config(
    *,
    include_patterns: tuple[str, ...] = (),
    exclude_patterns: tuple[str, ...] = (),
    exclude_manual_assets: bool = False,
) -> None:
    global _CONFIG

    if _CONFIG is not None:
        logging.warning('Config already initialized.')
        return

    _CONFIG = compile_cfg(
        CONFIG_DIR.resolve(),
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
        exclude_manual_assets=exclude_manual_assets,
    )

    if not _CONFIG.layers:
        raise exc.QgrNoLayersFoundError(
            'No layers found matching patterns:'
            f' "{include_patterns=}"; "{exclude_patterns=}.',
        )


@cache
def get_config() -> Config:
    if _CONFIG is None:
        raise RuntimeError('Config not initialized. Run `init_config` first!')

    return _CONFIG
