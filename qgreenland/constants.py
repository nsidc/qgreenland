import os
from enum import Enum

PROJECT = 'qgreenland'
DATA_DIR = '/luigi/data'
DATA_FINAL_DIR = f'/luigi/data/{PROJECT}'

# TMP_DIR is the same as DATA_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = DATA_DIR

# TODO: Figure out a way to use layers.yml or get rid of it
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
# LAYER_BASE_DIR = os.path.abspath(os.path.join(THIS_DIR, '../qgis-data/qgreenland/'))


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = 'fetch'

    # For still-processing data in temporary directory structure.
    WIP = 'wip'

    # For processed QGreenland data in its final directory structure.
    FINAL = f'{PROJECT}'
