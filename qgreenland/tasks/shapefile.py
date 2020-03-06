import os
import zipfile

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerConfigMixin
from qgreenland.util.misc import temporary_path_dir
from qgreenland.util.shapefile import (find_shapefile_in_dir,
                                       reproject_shapefile,
                                       subset_shapefile)


# TODO: Is there any task history? e.g. can we look at the final output target
# and generate a list of tasks that were performed to generate it?

class UnzipShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/unzip/')

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            zf = zipfile.ZipFile(self.input().path)

            for fn in zf.namelist():
                zf.extract(fn, temp_path)
            zf.close()


class ReprojectShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        # NOTE: Currently self.outdir is:
        # '/luigi/data/luigi-wip/wip/glacier_terminus'
        # Do we want to write to:
        # '/luigi/data/luigi-wip/wip/glacier_terminus/2006_2007/reproject'
        # ? If so, do we generate this based on the input path? Or based on the config?
        # Start with using the input path, then think about updating the config.
        # Can we put that logic in the LayerConfigMixin?
        return luigi.LocalTarget(f'{self.outdir}/reproject/')

    def run(self):
        breakpoint()
        shapefile = find_shapefile_in_dir(self.input().path)

        gdf = reproject_shapefile(shapefile)
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, 'shapefile.shp')
            gdf.to_file(fn, driver='ESRI Shapefile')


class SubsetShapefile(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/subset/')

    def run(self):
        shapefile = find_shapefile_in_dir(self.input().path)

        gdf = subset_shapefile(shapefile)
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, 'shapefile.shp')
            gdf.to_file(fn, driver='ESRI Shapefile')
