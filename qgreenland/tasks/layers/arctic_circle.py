from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.shapefile import (ReprojectShapefile,
                                               SubsetShapefile,
                                               Ogr2OgrShapefile)
from qgreenland.util.luigi import LayerPipeline


class ArcticCircle(LayerPipeline):

    def requires(self):
        fetch_data = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        ) # -> 
        to_shapefile = Ogr2OgrShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        ) # -> 
        reproject_shapefile = ReprojectShapefile(
            requires_task=to_shapefile,
            layer_id=self.layer_id
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )
