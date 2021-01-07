from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import GdalEdit, WarpRaster
from qgreenland.util.luigi import LayerPipeline


class SeaIceAge(LayerPipeline):
    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
        )  # ->
        gdal_edited = GdalEdit(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id,
        )  # ->
        return WarpRaster(
            requires_task=gdal_edited,
            layer_id=self.layer_id
        )
