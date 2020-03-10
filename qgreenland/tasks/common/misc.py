"""common.py: Tasks that could apply to any type of dataproduct."""
import glob
import os

import luigi
from osgeo import gdal

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerConfigMixin


class ExtractNcDataset(LayerConfigMixin, luigi.Task):
    """Extracts dataset `dataset_name` from input .nc file."""

    task_type = TaskType.WIP
    dataset_name = luigi.Parameter()
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        # GDAL translate will automatically determine file type from the extension.
        ext = self.layer_cfg['file_type']
        return luigi.LocalTarget(
            os.path.join(self.outdir, 'extract', f'{self.dataset_name}.{ext}')
        )

    def run(self):
        with self.output().open('w') as f:
            nc_files = glob.glob(os.path.join(self.input().path, '*.nc'))
            if len(nc_files) > 1:
                raise NotImplementedError('Handling of >1 .nc file not implemented')

            input_file = nc_files[0]
            gdal.Translate(
                f.buffer.name,
                f'NETCDF:{input_file}:{self.dataset_name}'
            )
