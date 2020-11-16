from qgreenland.tasks.common.fetch import FetchOgrRemoteData
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class OgrRemoteVector(LayerPipeline):
    def requires(self):
        fetch_data = FetchOgrRemoteData(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        return Ogr2OgrVector(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
