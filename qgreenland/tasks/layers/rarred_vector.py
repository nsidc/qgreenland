from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import Unrar
from qgreenland.tasks.common.vector import Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class RarredVector(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unrar = Unrar(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return Ogr2OgrVector(
            requires_task=unrar,
            layer_id=self.layer_id
        )
