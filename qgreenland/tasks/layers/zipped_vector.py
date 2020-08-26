from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import Unzip
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class ZippedVector(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return Ogr2OgrVector(
            requires_task=unzip,
            layer_id=self.layer_id
        )
