import logging
import os
import subprocess

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.shapefile import (filter_shapefile,
                                       reproject_shapefile,
                                       subset_shapefile)

logger = logging.getLogger('luigi-interface')


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
        gdf = reproject_shapefile(shapefile, layer_cfg=self.layer_cfg)

        # TODO: Dissolve polygon boundaries if required by config file

        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')


class SubsetShapefile(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/subset/')

    def run(self):
        shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            subset_shapefile(shapefile, layer_cfg=self.layer_cfg, outfile=fn)


class FilterShapefileFeatures(LayerTask):
    task_type = TaskType.WIP
    filter_func = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/filter/')

    def run(self):
        logger.info(f"Filtering {self.layer_cfg['id']}...")
        shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
        gdf = filter_shapefile(
            shapefile,
            filter_func=self.filter_func
        )

        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')


class Ogr2OgrShapefile(LayerTask):
    """Acts on vector data that can be read by `ogr2ogr`"""
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform/')

    def run(self):
        if (ogr2ogr_kwargs := self.layer_cfg.get('ogr2ogr_kwargs')) is None:
            raise RuntimeError('`Ogr2OgrShapefile` task requires `ogr2ogr_kwargs` in the layer config.')
            
        input_filename = ogr2ogr_kwargs.pop('input_filename')
        infile = os.path.join(self.input().path, input_filename)

        cmd_args_list = []
        for k, v in ogr2ogr_kwargs.items():
            cmd_args_list.append(f'-{k} {v}')

        cmd_args_str = ' '.join(cmd_args_list)

        with temporary_path_dir(self.output()) as temp_path:
            outfile = os.path.join(temp_path, f'{os.path.splitext(input_filename)[0]}.shp')
            cmd = f". activate base && ogr2ogr {cmd_args_str} {outfile} {infile}"

            result = subprocess.run(cmd,
                                    shell=True,
                                    executable='/bin/bash',
                                    capture_output=True)

        if result.returncode != 0:
            raise RuntimeError(result.stderr)
