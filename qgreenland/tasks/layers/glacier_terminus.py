from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.shapefile import Ogr2OgrShapefile
from qgreenland.util.luigi import LayerPipeline


class GlacierTerminus(LayerPipeline):
    """Dataproduct NSIDC-0642.

    https://nsidc.org/data/NSIDC-0642
    """

    def requires(self):
        fetch_data = FetchCmrGranule(source_cfg=self.cfg['source'],
                                     dataset_cfg=self.cfg['dataset'])
        return Ogr2OgrShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )
