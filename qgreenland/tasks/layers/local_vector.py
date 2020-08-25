from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class LocalVector(LayerPipeline):
    """Read any ogr2ogr-supported vector data."""

    def requires(self):
        fetch_data = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        return Ogr2OgrVector(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
