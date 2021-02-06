from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import BuildRasterOverviews, WarpRaster
from qgreenland.util.luigi import LayerPipeline


class BedMachineDataset(LayerPipeline):
    """Dataproduct IDBMG4.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.

    https://nsidc.org/data/IDBMG4
    """

    def requires(self):
        fetch_data = FetchCmrGranule(
            dataset_cfg=self.cfg['dataset'],
            source_cfg=self.cfg['source'],
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
        )  # ->
        warp_raster = WarpRaster(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
