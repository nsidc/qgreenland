from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.shapefile import Ogr2OgrShapefile
from qgreenland.util.luigi import LayerPipeline


class OnlineVector(LayerPipeline):
    """Download and process any vector data that ogr2ogr can read."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        return Ogr2OgrShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
