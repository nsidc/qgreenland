import logging
import os

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import (find_single_file_by_ext,
                                  find_single_file_by_name,
                                  temporary_path_dir)
from qgreenland.util.vector import cleanup_valid_datafiles, ogr2ogr, points_txt_to_shape

logger = logging.getLogger('luigi-interface')


class DelimitedTextPointsVector(LayerTask):
    """Acts on point vector data that is stored in a delimited text file.

    `header` defaults to 0 (first column),
    `delimiter` defaults to `,`
    `x_field` defaults to `latitude`
    `y_field` defaults to `longitude`
    """

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform_delimited/')

    def run(self):
        delimited_text_vector_kwargs = self.layer_cfg['delimited_text_vector_kwargs']

        if 'input_filename' in delimited_text_vector_kwargs:
            input_filepath = os.path.join(
                self.input().path,
                delimited_text_vector_kwargs.pop('input_filename')
            )
        else:
            text_file = find_single_file_by_ext(self.input().path, ext='.txt')
            input_filepath = text_file

        input_filename = os.path.basename(input_filepath)
        with temporary_path_dir(self.output()) as temp_path:
            infile = os.path.join(self.input().path, input_filename)

            file_ext = self.layer_cfg['file_type']
            out_filename = os.path.splitext(input_filename)[0] + file_ext
            outfile = os.path.join(temp_path, out_filename)
            points_txt_to_shape(
                infile, outfile,
                header=delimited_text_vector_kwargs.get('header', 0),
                delimiter=delimited_text_vector_kwargs.get('delimiter', ','),
                field_names=delimited_text_vector_kwargs.get('field_names'),
                x_field=delimited_text_vector_kwargs.get('x_field', 'latitude'),
                y_field=delimited_text_vector_kwargs.get('y_field', 'longitude')
            )


class Ogr2OgrVector(LayerTask):
    """Acts on vector data that can be read by `ogr2ogr`."""

    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/transform/')

    def run(self):
        input_ogr2ogr_kwargs = self.layer_cfg.get('ogr2ogr_kwargs', {})
        boundary_fp = self.layer_cfg['boundary']['fp']

        ogr2ogr_kwargs = {
            # Output an UTF-8 encoded data file instead of default ISO-8859-1
            'lco': 'ENCODING=UTF-8',
            't_srs': CONFIG['project']['crs'],
            # As opposed to `clipsrc`, `clipdst` uses the destination SRS
            # (`t_srs`) to clip the input after reprojection.
            'clipdst': boundary_fp,
        }
        ogr2ogr_kwargs.update(input_ogr2ogr_kwargs)

        if 'input_filename' in ogr2ogr_kwargs:
            input_filename = find_single_file_by_name(
                self.input().path,
                filename=ogr2ogr_kwargs.pop('input_filename')
            )
        else:
            # TODO: we assume input data comes in .shp format unless we override
            # the input_filename, but maybe we should have a list of possible
            # extensions we look for, starting with self.layer_cfg['file_type']?
            datafile = find_single_file_by_ext(
                self.input().path,
                ext='shp'
            )
            input_filename = datafile

        with temporary_path_dir(self.output()) as temp_path:
            # Before doing the requested transformation, make the vector data
            # valid. We have to do the SQL step here because this command will
            # change the internal table name of the output datafile.
            infile = os.path.join(self.input().path, input_filename)
            # TODO probably need to cleanup this output? Put it in another dir?
            valid_outfile = os.path.join(
                temp_path,
                f"valid.{self.layer_cfg['file_type']}"
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
            cleanup_valid_datafiles(
                temp_path,
                extensions=[self.layer_cfg['file_type']]
            )
