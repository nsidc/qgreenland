from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.shapefile import Ogr2OgrShapefile
from qgreenland.util.luigi import LayerPipeline


# TODO: Rename to remove "shapefile" -- this makes a shapefile but doesn't _have
# to_ take one as input -- "Local" refers to local storage of input, "Shapefile"
# refers to the output format. A bit confusing.
# -> LocalVector.
class LocalShapefile(LayerPipeline):
    """Read any ogr2ogr-supported vector data."""

    def requires(self):
        fetch_data = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        return Ogr2OgrShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
