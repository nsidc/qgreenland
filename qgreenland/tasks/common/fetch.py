import os
import shutil

import luigi

from qgreenland.constants import ASSETS_DIR, TaskType
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.misc import fetch_and_write_file, temporary_path_dir


class FetchTask(luigi.Task):
    dataset_cfg = luigi.DictParameter()
    source_cfg = luigi.DictParameter()

    @property
    def output_name(self):
        return f"{self.dataset_cfg['id']}.{self.source_cfg['id']}"


class FetchCmrGranule(FetchTask):
    session = None

    def output(self):
        path = [TaskType.FETCH.value, self.output_name]
        if 'subdir_path' in self.source_cfg:
            path.append(self.source_cfg['subdir_path'])

        return luigi.LocalTarget(os.path.join(*path))

    def run(self):
        granule = get_cmr_granule(
            granule_ur=self.source_cfg['granule_ur'],
            collection_concept_id=self.source_cfg['collection_concept_id'])

        with temporary_path_dir(self.output()) as temp_path:
            for url in granule.urls:
                if not self.session:
                    self.session = make_session(hosts=[url])

                fetch_and_write_file(url, output_dir=temp_path, session=self.session)


class FetchDataFiles(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop
        )

    def run(self):
        if self.dataset_cfg['access_method'] == 'cmr':
            raise RuntimeError('Use a FetchCmrGranule task!')

        with temporary_path_dir(self.output()) as temp_path:
            for url in self.source_cfg['urls']:
                fetch_and_write_file(url, output_dir=temp_path)


class FetchLocalDataFiles(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            for filename in self.source_cfg['urls']:
                source_path = os.path.join(ASSETS_DIR, 'local_data', filename)
                out_path = os.path.join(temp_path, os.path.basename(filename))

                shutil.copy2(source_path, out_path)
