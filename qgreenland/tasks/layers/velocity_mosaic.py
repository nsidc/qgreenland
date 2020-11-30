import os
import subprocess

import luigi

from qgreenland.constants import TaskType
from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.raster import (BuildRasterOverviews,
                                            WarpRaster)
from qgreenland.util.luigi import LayerPipeline
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir


class GdalCalcMaskedVelocity(LayerTask):
    """Mask ice velocity with included ice mask.

    Layer task specific for VelocityMosaic. Mask the velocity data with the ice
    mask included with the dataset. The ice mask is a binary grid where values
    of 1 indicate valid ice and values of 0 represent non-ice areas.

    TODO: get rid of this!!! Handle more complex workflows w/ existing tasks!
    Added this task to apply the ice mask to the velocity data, which itself is
    not masked...
    """

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'calc'))

    def run(self):
        with temporary_path_dir(self.output()) as tmp_dir:
            out_path = os.path.join(tmp_dir, self.filename)
            # TODO: figure this out lol
            inp_path = find_single_file_by_ext(self.input().path,
                                               ext='.nc')

            try:
                variable = self.layer_cfg['translate_kwargs']['extract_dataset']
            except KeyError:
                raise RuntimeError(
                    'Missing layer config for ITS_LIVE velocity mosiac: Needs `translate_kwargs:extract_dataset`'
                )

            cmd = (
                f'gdal_calc.py -A NETCDF:{inp_path}:{variable} -B NETCDF:{inp_path}:ice'
                f'  --calc="A*B" --outfile={out_path}'
            )
            result = subprocess.run(cmd,
                                    shell=True,
                                    executable='/bin/bash',
                                    capture_output=True)

            if result.returncode != 0:
                raise RuntimeError(result.stderr)


class VelocityMosaic(LayerPipeline):
    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        gdal_calc = GdalCalcMaskedVelocity(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        warp_raster = WarpRaster(
            requires_task=gdal_calc,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
