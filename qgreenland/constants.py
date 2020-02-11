import os
from enum import Enum

PROJECT = 'qgreenland'
DATA_DIR = '/luigi/data'
DATA_FINAL_DIR = f'{DATA_DIR}/{PROJECT}'
DATA_RELEASE_DIR = f'{DATA_DIR}/release'

# TMP_DIR is the same as DATA_DIR because os.rename doesn't allow cross-mount
# renaming. Make it a subdir?
TMP_DIR = DATA_DIR

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
REQUEST_TIMEOUT = 3

# Project configuration
# NOTE: The order of this dictionary is important for passing to qgc.QgsRectangle
BBOX = {'xmin': -3850000.000, 'ymin': -5350000.0, 'xmax': 3750000.0, 'ymax': 5850000.000}
BBOX_POLYGON = [
    (BBOX['xmin'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymax']),
    (BBOX['xmax'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymin']),
    (BBOX['xmin'], BBOX['ymax']),
]
PROJECT_CRS = 'EPSG:3411'

# URS stuff
URS_COOKIE = 'urs_user_already_logged'


class TaskType(Enum):
    """Task types determine the directory outputs are saved to."""

    # For downloading data. By keeping this in its own directory, we can
    # selectively avoid cleaning it up.
    FETCH = 'fetch'

    # For still-processing data in temporary directory structure.
    WIP = 'wip'

    # For processed QGreenland data in its final directory structure.
    FINAL = f'{PROJECT}'
