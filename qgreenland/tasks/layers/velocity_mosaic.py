import luigi

from qgreenland.tasks.common.fetch import FetchDataFile
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import ReprojectRaster
from qgreenland.util.luigi import LayerPipeline


class VelocityMosaic(LayerPipeline):
    """Dataset VelocityMosaic

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.
    """

    extract_dataset = luigi.Parameter()

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchDataFile(
            source_cfg=source,
            output_name='bedmachine'
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
            dataset_name=self.extract_dataset
        )  # ->
        return ReprojectRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )
