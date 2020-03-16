import os
import zipfile

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.shapefile import reproject_shapefile, subset_shapefile


class UnzipShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/unzip/')

    def run(self):
        zf_path = find_single_file_by_ext(self.input().path, ext='.zip')
        zf = zipfile.ZipFile(zf_path)

        with temporary_path_dir(self.output()) as temp_path:
            for fn in zf.namelist():
                zf.extract(fn, temp_path)
            zf.close()


class ReprojectShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        # TODO: DRY this out. Place responsibility in LayerTask.
        out_dir = os.path.join(
            self.outdir,
            'reproject',
            self.id
        )
        return luigi.LocalTarget(out_dir)

    def run(self):
        shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
        gdf = reproject_shapefile(shapefile)
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')


class SubsetShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/subset/')

    def run(self):
        shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
        gdf = subset_shapefile(shapefile, layer_cfg=self.layer_cfg)

        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')
