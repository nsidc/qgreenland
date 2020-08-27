import luigi

from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset, Unzip
from qgreenland.tasks.common.raster import BuildRasterOverviews, WarpRaster
from qgreenland.util.luigi import LayerPipeline


class ZippedNetCdf(LayerPipeline):
    """Rename files to their final location."""

    extract_dataset = luigi.Parameter()

    def requires(self):
        fetch_data = FetchDataFiles(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=unzip,
            layer_id=self.layer_id,
            dataset_name=self.extract_dataset
        )  # ->
        warp_raster = WarpRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
