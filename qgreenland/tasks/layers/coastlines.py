import os

from qgreenland.tasks.common.common import FetchDataFile
from qgreenland.tasks.common.shapefile import (ReprojectShapefile,
                                               SubsetShapefile,
                                               UnzipShapefile)
from qgreenland.util.luigi import LayerPipeline
from qgreenland.util.misc import temporary_path_dir
from qgreenland.util.shapefile import find_shapefile_in_dir


class Coastlines(LayerPipeline):
    """Rename files to their final location."""

    layer_id = 'coastlines'

    def requires(self):
        fetch_data = FetchDataFile(
            # TODO: Make this in to a for loop over `sources`
            source_cfg=self.cfg['sources'][0],
            output_name=self.cfg['short_name']
        )  # ->
        unzip_shapefile = UnzipShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=unzip_shapefile,
            layer_id=self.layer_id
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )

    def run(self):
        shapefile = find_shapefile_in_dir(self.input().path)
        processed_shapefile_dir = os.path.dirname(shapefile)

        with temporary_path_dir(self.output()) as temp_path:
            for f in os.listdir(processed_shapefile_dir):
                _, ext = f.split('.')
                old_fp = os.path.join(processed_shapefile_dir, f)
                new_fp = os.path.join(
                    temp_path,
                    f'{self.layer_id}.{ext}')

                os.rename(old_fp, new_fp)
