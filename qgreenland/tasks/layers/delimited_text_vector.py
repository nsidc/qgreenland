from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.vector import DelimitedTextPointsVector, Ogr2OgrVector
from qgreenland.util.luigi import LayerPipeline


class DelimitedTextVector(LayerPipeline):
    def requires(self):
        fetch_data = FetchDataFiles(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        delimited_text_vector = DelimitedTextPointsVector(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return Ogr2OgrVector(
            requires_task=delimited_text_vector,
            layer_id=self.layer_id
        )
