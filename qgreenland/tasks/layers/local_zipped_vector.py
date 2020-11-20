from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.misc import Unzip
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class LocalZippedVector(LayerPipeline):
    """Read any ogr2ogr-supported vector data."""

    def requires(self):
        fetch_data = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return Ogr2OgrVector(
            requires_task=unzip,
            layer_id=self.layer_id
        )
