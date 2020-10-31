from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.raster import GdalEdit, GdalMDimTranslate
from qgreenland.util.luigi import LayerPipeline


class BasalThermalState(LayerPipeline):
    """Dataset BasalThermalState.

    https://nsidc.org/data/rdbts4/versions/1
    """

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        mdim_translate = GdalMDimTranslate(
            requires_task=fetch_data,
            input_ext_override='nc',
            layer_id=self.layer_id,
        )  # ->
        return GdalEdit(
            requires_task=mdim_translate,
            layer_id=self.layer_id,
        )
