from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.raster import ReprojectRaster
from qgreenland.util.luigi import LayerPipeline


class ArcticVegetation(LayerPipeline):
    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            output_name='arctic_vegetation'
        )  # ->
        return ReprojectRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
