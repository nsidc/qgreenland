import logging
import os

import luigi

from qgreenland.constants import CONFIG, TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.vector import filter_vector, ogr2ogr

logger = logging.getLogger('luigi-interface')


# TODO: Make more generic -- filter vector features, don't assume .shp
# TODO: Use Ogr2OgrVector to filter with sql instead of lambda?
class FilterShapefileFeatures(LayerTask):
    """Expects a shapefile as input and writes a shapefile out."""

    task_type = TaskType.WIP
    filter_func = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/filter/')

    def run(self):
        logger.info(f"Filtering {self.layer_cfg['id']}...")
        shapefile = find_single_file_by_ext(self.input().path, ext='.shp')
        gdf = filter_vector(
            shapefile,
            filter_func=self.filter_func
        )

        with temporary_path_dir(self.output()) as temp_path:
            fn = os.path.join(temp_path, self.filename)
            gdf.to_file(fn, driver='ESRI Shapefile')


class Ogr2OgrVector(LayerTask):
    """Acts on vector data that can be read by `ogr2ogr`."""

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform/')

    def run(self):
        input_ogr2ogr_kwargs = self.layer_cfg.get('ogr2ogr_kwargs', {})

        # Extract the extent from the config, defaulting to 'background'.
        layer_extent_str = self.layer_cfg.get('extent', 'background')
        extent = CONFIG['project']['extents'][layer_extent_str]
        clipdst = ('"{xmin}" "{ymin}" '
                   '"{xmax}" "{ymax}"').format(**extent)  # noqa: FS002
        ogr2ogr_kwargs = {
            # Output an UTF-8 encoded shapefile instead of default ISO-8859-1
            'lco': 'ENCODING=UTF-8',
            't_srs': CONFIG['project']['crs'],
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
            # Before doing the requested transformation, make the vector data
            # valid. We have to do the SQL step here because this command will
            # change the internal table name of the output shapefile.
            infile = os.path.join(self.input().path, input_filename)
            # TODO probably need to cleanup this output? Put it in another dir?
            valid_outfile = os.path.join(
                temp_path,
                'valid.shp'
            )
            valid_kwargs = {'makevalid': ''}
            if 'sql' in ogr2ogr_kwargs:
                valid_kwargs['sql'] = ogr2ogr_kwargs.pop('sql')
            ogr2ogr(infile, valid_outfile, **valid_kwargs)
            infile = valid_outfile

            # Do the requested transformation
            outfile = os.path.join(
                temp_path,
                self.filename
            )
            ogr2ogr(infile, outfile, **ogr2ogr_kwargs)
