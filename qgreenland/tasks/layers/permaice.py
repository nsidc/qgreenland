from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.raster import WarpRaster
from qgreenland.util.luigi import LayerPipeline


class Permaice(LayerPipeline):
    """Dataproduct GGD318.

    https://nsidc.org/data/GGD318/versions/2
    """

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset'],
        )  # ->
        return WarpRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id,
            input_ext_override='.byte'
        )
