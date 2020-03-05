"""common.py: Tasks that could apply to any type of dataproduct."""
import os

import luigi
from osgeo import gdal

from qgreenland.constants import TaskType
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.luigi import LayerConfigMixin
from qgreenland.util.misc import fetch_file, temporary_path_dir


class FetchCmrGranule(luigi.Task):
    source_cfg = luigi.DictParameter()
    output_name = luigi.Parameter()

    session = None

    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                TaskType.FETCH.value,
                self.output_name,
                self.source_cfg['subdir_path']
            )
        )

    def run(self):
        granule = get_cmr_granule(granule_ur=self.source_cfg['granule_ur'])

        with temporary_path_dir(self.output()) as temp_path:
            for url in granule.urls:
                if not self.session:
                    self.session = make_session(hosts=[url])

                fn = os.path.basename(url)
                fp = os.path.join(temp_path, fn)

                resp = fetch_file(url, session=self.session)
                with open(fp, 'wb') as f:
                    f.write(resp.content)


class FetchDataFile(luigi.Task):
    source_cfg = luigi.DictParameter()
    output_name = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name,
                         f'{self.output_name}.data'),
            format=luigi.format.Nop
        )

    def run(self):
        if 'cmr' in self.source_cfg:
            granules = CmrGranules(
                self.source_cfg['cmr']['short_name'],
                self.source_cfg['cmr']['version']
            )
            urls = [g.url for g in granules]
            url = urls[0]
        elif 'url' in self.source_cfg:
            url = self.source_cfg['url']

        resp = fetch_file(url)
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)


class ExtractNcDataset(LayerConfigMixin, luigi.Task):
    """Extracts dataset `dataset_name` from input .nc file."""

    task_type = TaskType.WIP
    dataset_name = luigi.Parameter()
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        # GDAL translate will automatically determine file type from the extension.
        ext = self.layer_cfg['file_type']
        return luigi.LocalTarget(
            os.path.join(self.outdir, 'extract', f'{self.dataset_name}.{ext}')
        )

    def run(self):
        with self.output().open('w') as f:
            gdal.Translate(
                f.buffer.name,
                f'NETCDF:{self.input().path}:{self.dataset_name}'
            )
