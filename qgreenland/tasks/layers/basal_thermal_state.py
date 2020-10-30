from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.raster import GdalEdit, GdalMDimTranslate
from qgreenland.util.luigi import LayerPipeline


class BasalThermalState(LayerPipeline):
    """Dataset VelocityMosaic.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.
    """

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        # extract_nc_dataset = ExtractNcDataset(
        #     requires_task=fetch_data,
        #     layer_id=self.layer_id,
        # )  # ->
        mdim_translate = GdalMDimTranslate(
            requires_task=fetch_data,
            input_ext_override='nc',
            layer_id=self.layer_id,
        )  # ->
        return GdalEdit(
            requires_task=mdim_translate,
            layer_id=self.layer_id,
        )
