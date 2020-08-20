from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.raster import (BuildRasterOverviews,
                                            GdalCalcRaster,
                                            WarpRaster)
from qgreenland.util.luigi import LayerPipeline


class RasterCalc(LayerPipeline):
    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        gdal_calc = GdalCalcRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        warp_raster = WarpRaster(
            requires_task=gdal_calc,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
