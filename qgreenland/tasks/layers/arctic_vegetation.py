from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.raster import WarpRaster
from qgreenland.util.luigi import LayerPipeline


class ArcticVegetation(LayerPipeline):
    def requires(self):
        fetch_data = FetchCmrGranule(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        return WarpRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
