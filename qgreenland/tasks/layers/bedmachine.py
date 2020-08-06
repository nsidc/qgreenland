import luigi

from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import WarpRaster
from qgreenland.util.luigi import LayerPipeline


class BedMachineDataset(LayerPipeline):
    """Dataproduct IDBMG4.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.

    https://nsidc.org/data/IDBMG4
    """

    extract_dataset = luigi.Parameter()

    # TODO remove.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_id = f'bedmachine_{self.extract_dataset}'

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            output_name='bedmachine'
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
            dataset_name=self.extract_dataset
        )  # ->
        return WarpRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )
