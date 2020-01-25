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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        short_name = self.layer_cfg['short_name']
        # TODO may not always be .tif
        self.outfile = f'{DATA_WIP_DIR}/{short_name}/reprojected.tif'

    def requires(self):
        return FetchData(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(self.outfile)

    def run(self):
        gdal.Warp(self.output().path, self.input().path,
                  dstSRS=PROJECT_CRS,
                  resampleAlg='bilinear')


class SubsetRaster(luigi.Task):
    layer_cfg = luigi.Parameter()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        short_name = self.layer_cfg['short_name']
        # TODO may not always be .tif
        self.outfile = f'{DATA_WIP_DIR}/{short_name}/subset.tif'


    def requires(self):
        return ReprojectRaster(self.layer_cfg)

    def output(self):
        return luigi.LocalTarget(self.outfile)

    def run(self):
        with rio.open(self.input().path, 'r') as ds:
            bb_poly = geopandas.GeoSeries([Polygon(BBOX_POLYGON)])
            img_out, meta_out = eps.crop_image(ds, bb_poly)

        with rio.open(self.output().path, 'w', **meta_out) as c_ds:
            c_ds.write(img_out)
