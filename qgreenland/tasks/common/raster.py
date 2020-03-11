import os
import shutil

import geopandas
import luigi
import rasterio as rio
from earthpy import spatial as eps
from osgeo import gdal
from shapely.geometry import Polygon

from qgreenland.constants import BBOX_POLYGON, PROJECT_CRS, TaskType
from qgreenland.util.luigi import LayerTask


class BuildRasterOverviews(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        of = os.path.join(self.outdir, 'overviews', self.filename)
        return luigi.LocalTarget(of)

    def run(self):
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

        with self.output().temporary_path() as tmp_path:
            # Copy the existing file into place. Currently, this task creates
            # 'internal overviews', which changes the file itself.
            shutil.copy2(self.input().path, tmp_path)

            with rio.open(tmp_path, 'r+') as ds:
                ds.build_overviews(overview_levels, resampling_method)


class ReprojectRaster(LayerTask):
    task_type = TaskType.WIP
    def output(self):
        of = os.path.join(self.outdir, 'reproject', self.filename)
        return luigi.LocalTarget(of)

    def run(self):
        with self.output().temporary_path() as tmp_path:
            warp_kwargs = {
                'resampleAlg': 'bilinear'
            }
            if 'warp_kwargs' in self.layer_cfg:
                warp_kwargs.update(self.layer_cfg['warp_kwargs'])

            gdal.Warp(tmp_path, self.input().path, dstSRS=PROJECT_CRS,
                      **warp_kwargs)


class SubsetRaster(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        of = os.path.join(self.outdir, 'subset', self.filename)
        return luigi.LocalTarget(of)

    def run(self):
        with rio.open(self.input().path, 'r') as ds:
            bb_poly = geopandas.GeoSeries([Polygon(BBOX_POLYGON)])
            img_out, meta_out = eps.crop_image(ds, bb_poly)

        with self.output().temporary_path() as tmp_path:
            with rio.open(tmp_path, 'w', **meta_out) as c_ds:
                c_ds.write(img_out)
