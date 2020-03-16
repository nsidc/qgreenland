from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.shapefile import (ReprojectShapefile,
                                               SubsetShapefile,
                                               UnzipShapefile)
from qgreenland.util.luigi import LayerPipeline


class ZippedShapefile(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        unzip_shapefile = UnzipShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=unzip_shapefile,
            layer_id=self.layer_id
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )
