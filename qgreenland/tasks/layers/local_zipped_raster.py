from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset, Unzip
from qgreenland.tasks.common.raster import WarpRaster
from qgreenland.util.luigi import LayerPipeline


class LocalZippedRaster(LayerPipeline):

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchLocalDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return WarpRaster(
            requires_task=unzip,
            layer_id=self.layer_id
        )
