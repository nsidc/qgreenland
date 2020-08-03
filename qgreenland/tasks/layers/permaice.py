from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.shapefile import ReprojectShapefile, SubsetShapefile
from qgreenland.util.luigi import LayerPipeline


class Permaice(LayerPipeline):
    """Dataproduct GGD318

    https://nsidc.org/data/GGD318/versions/2
    """
    # TODO: figure out how to keep the .avl file? Is the .avl file useful?

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )
