import logging
import os

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.vector import cleanup_valid_shapefile, ogr2ogr

logger = logging.getLogger('luigi-interface')


class Ogr2OgrVector(LayerTask):
    """Acts on vector data that can be read by `ogr2ogr`."""

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform/')

    def run(self):
        input_ogr2ogr_kwargs = self.layer_cfg.get('ogr2ogr_kwargs', {})
        boundary_fp = self.layer_cfg['boundary']['fp']

        ogr2ogr_kwargs = {
            # Output an UTF-8 encoded shapefile instead of default ISO-8859-1
            'lco': 'ENCODING=UTF-8',
            't_srs': CONFIG['project']['crs'],
            # As opposed to `clipsrc`, `clipdst` uses the destination SRS
            # (`t_srs`) to clip the input after reprojection.
            'clipdst': boundary_fp,
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

            # TODO: Make valid without writing to disk?
            cleanup_valid_shapefile(temp_path)
