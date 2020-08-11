import logging
import os

import luigi

from qgreenland.constants import PROJECT_CRS, PROJECT_EXTENT, TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.shapefile import filter_shapefile, ogr2ogr

logger = logging.getLogger('luigi-interface')


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
    """Acts on vector data that can be read by `ogr2ogr`."""

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform/')

    def run(self):
        input_ogr2ogr_kwargs = self.layer_cfg.get('ogr2ogr_kwargs', {})

        clipdst = ('"{xmin}" "{ymin}" '
                   '"{xmax}" "{ymax}"').format(**PROJECT_EXTENT)  # noqa: FS002
        ogr2ogr_kwargs = {
            't_srs': PROJECT_CRS,
            # As opposed to `clipsrc`, `clipdst` uses the destination SRS
            # (`t_srs`) to clip the input after reprojection.
            'clipdst': clipdst,
        }
        ogr2ogr_kwargs.update(input_ogr2ogr_kwargs)

        if 'input_filename' in ogr2ogr_kwargs:
            input_filename = os.path.join(
                self.input().path,
                ogr2ogr_kwargs.pop('input_filename')
            )
        else:
            shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
            input_filename = shapefile

        with temporary_path_dir(self.output()) as temp_path:
            infile = os.path.join(self.input().path, input_filename)
            outfile = os.path.join(
                temp_path,
                self.filename
            )

            ogr2ogr(infile, outfile, **ogr2ogr_kwargs)
