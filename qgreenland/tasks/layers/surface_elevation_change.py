from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.raster import GdalEdit, GdalMDimTranslate
from qgreenland.util.luigi import LayerPipeline


class CCISurfaceElevationChange(LayerPipeline):
    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchLocalDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        return GdalMDimTranslate(
            requires_task=fetch_data,
            input_ext_override='nc',
            layer_id=self.layer_id,
        )
