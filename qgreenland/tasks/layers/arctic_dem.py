import os

from qgreenland.tasks.common.common import FetchDataFile
from qgreenland.tasks.common.raster import (BuildRasterOverviews,
                                            ReprojectRaster,
                                            SubsetRaster)
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import temporary_path_dir


class ArcticDEM(LayerTask):
    """Rename files to their final location."""

    layer_id = 'arctic_dem'

    def requires(self):
        fetch_data = FetchDataFile(
            source_cfg=self.cfg['sources'][0],
            output_name=self.cfg['short_name']
        )  # ->
        reproject_raster = ReprojectRaster(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        subset_raster = SubsetRaster(
            requires_task=reproject_raster,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=subset_raster,
            layer_id=self.layer_id
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_id}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)
