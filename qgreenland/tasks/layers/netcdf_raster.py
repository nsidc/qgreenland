from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import BuildRasterOverviews, WarpRaster
from qgreenland.util.luigi import LayerPipeline


class NetCdfRaster(LayerPipeline):
    """Dataset VelocityMosaic.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.
    """

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
        )  # ->
        warp_raster = WarpRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
