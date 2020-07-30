"""common.py: Tasks that could apply to any type of dataproduct."""
import os
import zipfile

import luigi
import rarfile
from osgeo import gdal

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir


class Decompress(LayerTask):
    task_type = TaskType.WIP
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decompress_kwargs = self.layer_cfg.get('decompress_kwargs', {})

    def output(self):
        return luigi.LocalTarget(f'{self.outdir}/decompress/')


class Unrar(Decompress):
    def run(self):
        rar_path = find_single_file_by_ext(self.input().path, ext='.rar')
        rf = rarfile.RarFile(rar_path)

        with temporary_path_dir(self.output()) as temp_path:
            if 'extract_file' in self.decompress_kwargs:
                rf.extract(decompress_kwargs['extract_file'],
                           path=temp_path)
            else:
                rf.extractall(path=temp_path)

            rf.close()


class Unzip(Decompress):
    def run(self):
        zf_path = find_single_file_by_ext(self.input().path, ext='.zip')
        zf = zipfile.ZipFile(zf_path)

        with temporary_path_dir(self.output()) as temp_path:
            if 'extract_file' in self.decompress_kwargs:
                zf.extract(self.decompress_kwargs['extract_file'],
                           path=temp_path)
            else:
                # zf.extractall instead???
                for fn in zf.namelist():
                    zf.extract(fn, temp_path)

            zf.close()


class ExtractNcDataset(LayerTask):
    """Extracts dataset `dataset_name` from input .nc file."""

    task_type = TaskType.WIP
    dataset_name = luigi.Parameter()

    def output(self):
        # GDAL translate will automatically determine file type from the extension.
        return luigi.LocalTarget(
            os.path.join(self.outdir, 'extract')
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_dir:
            input_fp = find_single_file_by_ext(self.input().path, ext='.nc')

            output_filename = f"{self.dataset_name}{self.layer_cfg['file_type']}"
            output_fp = os.path.join(temp_dir, output_filename)

            gdal.Translate(
                output_fp,
                f'NETCDF:{input_fp}:{self.dataset_name}'
            )
