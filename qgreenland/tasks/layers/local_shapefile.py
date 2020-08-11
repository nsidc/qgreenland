from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.shapefile import Ogr2OgrShapefile
from qgreenland.util.luigi import LayerPipeline


class LocalShapefile(LayerPipeline):

    def requires(self):
        fetch_data = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        return Ogr2OgrShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
