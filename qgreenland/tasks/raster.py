import luigi

from osgeo import gdal
import rasterio as rio
import geopandas
from earthpy import spatial as eps
from shapely.geometry import Polygon

from qgreenland.constants import DATA_WIP_DIR
from qgreenland.tasks.common import FetchData
from qgreenland.util import PROJECT_CRS, BBOX_POLYGON


class ReprojectRaster(luigi.Task):
    layer_cfg = luigi.Parameter()

    def requires(self):
        return FetchData(self.layer_cfg)

    def output(self):
        # TODO may not always be .tif
        return luigi.LocalTarget(f"{DATA_WIP_DIR}/"
                                 "{self.layer_cfg['short_name']}_reprojected.tif")

    def run(self):
        gdal.Warp(self.output().path, self.input().path,
                  dstSRS=PROJECT_CRS,
                  resampleAlg='bilinear')


class SubsetRaster(luigi.Task):
    layer_cfg = luigi.Parameter()

    def requires(self):
        return ReprojectRaster(self.layer_cfg)

    def output(self):
        # TODO may not always be .tif
        return luigi.LocalTarget(f"{DATA_WIP_DIR}/"
                                 "{self.layer_cfg['short_name']}_subset.tif")

    def run(self):
        with rio.open(self.input().path, 'r') as ds:
            bb_poly = geopandas.GeoSeries([Polygon(BBOX_POLYGON)])
            img_out, meta_out = eps.crop_image(ds, bb_poly)

        with rio.open(self.output().path, 'w', **meta_out) as c_ds:
            c_ds.write(img_out)
