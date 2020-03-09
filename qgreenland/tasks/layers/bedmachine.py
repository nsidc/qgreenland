import os

import luigi

from qgreenland.tasks.common.common import ExtractNcDataset, FetchCmrGranule
from qgreenland.tasks.common.raster import ReprojectRaster
from qgreenland.util.luigi import LayerPipeline
from qgreenland.util.misc import temporary_path_dir


class BedMachineDataset(LayerPipeline):
    """Dataproduct IDBMG4.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.

    https://nsidc.org/data/IDBMG4
    """

    dataset_name = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_id = f'bedmachine_{self.dataset_name}'

    def requires(self):
        source = self.cfg['sources'][0]

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            output_name='bedmachine'
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
            dataset_name=self.dataset_name
        )  # ->
        return ReprojectRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_id}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)
