from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import Unzip
from qgreenland.tasks.common.raster import (BuildRasterOverviews,
                                            ReprojectRaster,
                                            SubsetRaster)
from qgreenland.util.luigi import LayerPipeline


class BackgroundImage(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        reproject_raster = ReprojectRaster(
            requires_task=unzip,
            layer_id=self.layer_id
        )  # ->
        return SubsetRaster(
            requires_task=reproject_raster,
            layer_id=self.layer_id
        )
        """
        return BuildRasterOverviews(
            requires_task=subset_raster,
            layer_id=self.layer_id
        )
        """
