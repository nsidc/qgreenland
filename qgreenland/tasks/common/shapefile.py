import os
import zipfile

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import temporary_path_dir
from qgreenland.util.shapefile import (find_shapefile_in_dir,
                                       reproject_shapefile,
                                       subset_shapefile)


# TODO: Is there any task history? e.g. can we look at the final output target
# and generate a list of tasks that were performed to generate it?

class UnzipShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/unzip/')

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            zf = zipfile.ZipFile(self.input().path)

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
        shapefile = find_shapefile_in_dir(self.input().path)

        gdf = reproject_shapefile(shapefile)
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')


class SubsetShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/subset/')

    def run(self):
        shapefile = find_shapefile_in_dir(self.input().path)

        gdf = subset_shapefile(shapefile)
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')
