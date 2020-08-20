from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.raster import BuildRasterOverviews, WarpRaster
from qgreenland.util.luigi import LayerPipeline


class Raster(LayerPipeline):
    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        warp_raster = WarpRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
