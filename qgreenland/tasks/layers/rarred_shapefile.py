from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import Unrar
from qgreenland.tasks.common.shapefile import (ReprojectShapefile,
                                               SubsetShapefile)
from qgreenland.util.luigi import LayerPipeline


class RarredShapefile(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        unrar = Unrar(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=unrar,
            layer_id=self.layer_id
        )  # ->
        # TODO: We don't always need/want to subset, so parameterize this
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )
