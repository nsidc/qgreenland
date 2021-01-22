from pathlib import Path

from qgreenland.config import CONFIG
from qgreenland.util.misc import get_layer_path, find_single_file_by_exts
from qgreenland.constants import TaskType

import rasterio as rio

for name, layer_cfg in CONFIG['layers'].items():
    # TODO: must be run in the container's context
    if layer_cfg['data_type'] != 'raster':
        continue

    dataset_cfg = layer_cfg['dataset']
    source_cfg = layer_cfg['source']
    fetch_dir =  Path(TaskType.FETCH.value) / f"{dataset_cfg['id']}.{source_cfg['id']}"

    # TODO: Some datasets are zipped...finding the correct input requires knowing
    # about the layer pipeline.
    input_filepath = find_single_file_by_exts(fetch_dir, exts=('.tif', '.nc'))
    output_filepath = get_layer_path(layer_cfg)

    breakpoint()
    print('whooop!')
