from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset, Unzip
from qgreenland.tasks.common.raster import GdalEdit
from qgreenland.util.luigi import LayerPipeline


# TODO: Rename to racmo_raster
class Racmo(LayerPipeline):

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchLocalDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=unzip,
            layer_id=self.layer_id,
        )  # ->
        return GdalEdit(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )
