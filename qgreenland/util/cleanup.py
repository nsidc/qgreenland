#!/usr/bin/env python
import os
import shutil
import time

from qgreenland.constants import (
    INPUT_DIR,
    OUTPUT_DIRS,
)


def cleanup_intermediate_dirs():
    """Delete all intermediate data, except 'fetch' dir."""
    for d in OUTPUT_DIRS:
        if d is not INPUT_DIR:
            _rmtree(d)

    # TODO: Delete this block? The context manager handles cleaning up the tmp
    # dirs, and this `x.startswith('tmp')` condition should never evaluate
    # `True`. The real temp dirs look like `foo-luigi-tmp-#####`.
    # if os.path.isdir(WIP_DIR):
    #     for x in os.listdir(WIP_DIR):
    #         if x.startswith('tmp'):
    #             _rmtree(x)


def _rmtree(directory, *, retries=3):
    """Add robustness to shutil.rmtree.

    Retries in case of intermittent issues, e.g. with network storage.
    """
    if os.path.isdir(directory):
        for i in range(retries):
            try:
                shutil.rmtree(directory)
                return
            except OSError as e:
                print(f'WARNING: shutil.rmtee failed for path: {directory}')
                print(f'Exception: {e}')
                print(f'Retrying in {i} seconds...')
                time.sleep(i)

        # Allow caller to receive exceptions raised on the final try
        shutil.rmtree(directory)
