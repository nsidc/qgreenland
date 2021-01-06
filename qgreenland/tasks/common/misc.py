"""common.py: Tasks that could apply to any type of dataproduct."""
import gzip
import logging
import os
import zipfile

import luigi
import rarfile
from osgeo import gdal

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import (find_in_dir_by_pattern,
                                  find_single_file_by_ext,
                                  find_single_file_by_name,
                                  temporary_path_dir)


logger = logging.getLogger('luigi-interface')


class Decompress(LayerTask):
    task_type = TaskType.WIP

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decompress_kwargs = self.layer_cfg.get('decompress_kwargs', {})

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/decompress/')


class UngzipMany(Decompress):
    def run(self):
        gzip_paths = find_in_dir_by_pattern(self.input().path, pattern='*.gz')
        with temporary_path_dir(self.output()) as temp_path:
            for gzip_path in gzip_paths:
                with gzip.open(gzip_path, 'rb') as gf:
                    decompress_filename = os.path.basename(gzip_path).replace('.gz', '')
                    decompress_filepath = os.path.join(temp_path, decompress_filename)
                    with open(decompress_filepath, 'wb') as f:
                        f.write(gf.read())


class Unrar(Decompress):
    def run(self):
        rar_path = find_single_file_by_ext(self.input().path, ext='.rar')
        rf = rarfile.RarFile(rar_path)

        with temporary_path_dir(self.output()) as temp_path:
            if 'extract_file' in self.decompress_kwargs:
                rf.extract(self.decompress_kwargs['extract_file'],
                           path=temp_path)
            else:
                rf.extractall(path=temp_path)

            rf.close()


class Unzip(Decompress):
    def run(self):
        if unzip_filename := self.layer_cfg.get('unzip_kwargs', {}).get('input_filename'):
            zf_path = find_single_file_by_name(self.input().path, filename=unzip_filename)
        else:
            zf_path = find_single_file_by_ext(self.input().path, ext='.zip')
        zf = zipfile.ZipFile(zf_path)

        with temporary_path_dir(self.output()) as temp_path:
            if 'extract_files' in self.decompress_kwargs:
                for extract_file in self.decompress_kwargs['extract_files']:
                    zf.extract(extract_file, path=temp_path)
            else:
                # zf.extractall instead???
                for fn in zf.namelist():
                    zf.extract(fn, temp_path)

            zf.close()


# TODO: Make generic GdalTranslate task instead!!!!!!!
class ExtractNcDataset(LayerTask):
    """Extracts dataset `dataset_name` from input .nc file."""

    task_type = TaskType.WIP

    def output(self):
        # GDAL translate will automatically determine file type from the extension.
        return luigi.LocalTarget(
            os.path.join(self.outdir, 'extract')
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_dir:
            input_fp = find_single_file_by_ext(self.input().path, ext='.nc')

            dataset_name = self.layer_cfg['translate_kwargs'].pop('extract_dataset')

            output_filename = f"{dataset_name}{self.layer_cfg['file_type']}"
            output_fp = os.path.join(temp_dir, output_filename)

            from_dataset_path = f'NETCDF:{input_fp}:{dataset_name}'
            logger.debug(
                f'Using gdal.Translate to convert from {from_dataset_path} to {output_fp}'
            )

            gdal.Translate(
                output_fp,
                from_dataset_path,
                **self.layer_cfg['translate_kwargs']
            )
