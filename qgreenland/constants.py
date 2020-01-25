import os

DATA_ROOT_DIR = '/luigi/data'

DATA_DOWNLOAD_DIR = f'{DATA_ROOT_DIR}/download'
DATA_WIP_DIR = f'{DATA_ROOT_DIR}/wip'
DATA_FINAL_DIR = f'{DATA_ROOT_DIR}/qgreenland'
TMP_DIR = DATA_ROOT_DIR

# TODO: Figure out a way to use layers.yml or get rid of it
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
# LAYER_BASE_DIR = os.path.abspath(os.path.join(THIS_DIR, '../qgis-data/qgreenland/'))
