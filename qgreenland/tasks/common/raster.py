import os
import shutil

import geopandas
import luigi
import rasterio as rio
from earthpy import spatial as eps
from osgeo import gdal
from shapely.geometry import Polygon

from qgreenland.constants import PROJECT_CRS, PROJECT_EXTENT, TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.shapefile import bbox_dict_to_polygon


class BuildRasterOverviews(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'overviews'))

    def run(self):
        # TODO: Extract this to LayerTask as a property?
        # TODO: Find in dir by self.filename instead? Wouldn't work if the
        #       upstream task was e.g. unzip
        ifile = find_single_file_by_ext(self.input().path,
                                        ext=self.layer_cfg['file_type'])

        overviews_kwargs = {
            'overview_levels': (2, 4, 8, 16),
            'resampling_method': 'average'
        }

        overviews_kwargs.update(
            self.layer_cfg.get('overviews_kwargs', {})
        )

        overview_levels = overviews_kwargs['overview_levels']
        resampling_str = overviews_kwargs['resampling_method']

        try:
            resampling_method = rio.enums.Resampling[resampling_str]
        except KeyError:
            raise RuntimeError(
                f"'{resampling_str}' is not a valid resampling method."
            )

        with temporary_path_dir(self.output()) as tmp_dir:
            tmp_path = os.path.join(tmp_dir, self.filename)
            # Copy the existing file into place. Currently, this task creates
            # 'internal overviews', which changes the file itself.
            shutil.copy2(ifile, tmp_path)

            with rio.open(tmp_path, 'r+') as ds:
                ds.build_overviews(overview_levels, resampling_method)


class ReprojectRaster(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'reproject'))

    def run(self):
        warp_kwargs = {
            'resampleAlg': 'bilinear'
        }
        if 'warp_kwargs' in self.layer_cfg:
            warp_kwargs.update(self.layer_cfg['warp_kwargs'])

        ifile = find_single_file_by_ext(self.input().path,
                                        ext=self.layer_cfg['file_type'])

        with temporary_path_dir(self.output()) as tmp_dir:
            tmp_path = os.path.join(tmp_dir, self.filename)
            gdal.Warp(tmp_path, ifile, dstSRS=PROJECT_CRS, **warp_kwargs)


class SubsetRaster(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'subset'))

    def run(self):
        ifile = find_single_file_by_ext(self.input().path,
                                        ext=self.layer_cfg['file_type'])

        with rio.open(ifile, 'r') as ds:
            polygon = bbox_dict_to_polygon(PROJECT_EXTENT)
            bb_poly = geopandas.GeoSeries([polygon])
            img_out, meta_out = eps.crop_image(ds, bb_poly)

        with temporary_path_dir(self.output()) as tmp_dir:
            tmp_path = os.path.join(tmp_dir, self.filename)
            with rio.open(tmp_path, 'w', **meta_out) as c_ds:
                c_ds.write(img_out)
