import os
import shutil

import luigi

from qgreenland.constants import LOCALDATA_DIR, PRIVATE_ARCHIVE_DIR, TaskType
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.misc import fetch_and_write_file, temporary_path_dir
from qgreenland.util.vector import ogr2ogr


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
        # TODO: better
        # TODO: currently have this setup so that the local archive is nested
        # under dataset_id.
        if self.dataset_cfg['access_method'] == 'local':
            local_dir = LOCALDATA_DIR
        elif self.dataset_cfg['access_method'] == 'private-archive':
            local_dir = os.path.join(PRIVATE_ARCHIVE_DIR, self.dataset_cfg['id'])
        else:
            # TODO: use appropraite error or avoid this conditional.
            raise RuntimeError('NOOOOOOOOO')

        with temporary_path_dir(self.output()) as temp_path:
            for filename in self.source_cfg['urls']:
                source_path = os.path.join(local_dir, filename)
                out_path = os.path.join(temp_path, os.path.basename(filename))

                shutil.copy2(source_path, out_path)


class FetchOgrRemoteData(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            url = self.source_cfg['query_url']

            ofile = os.path.join(temp_path, 'fetched.geojson')
            ogr2ogr_kwargs = {
                'oo': 'FEATURE_SERVER_PAGING=YES',
            }

            ogr2ogr(f'"{url}"', ofile, **ogr2ogr_kwargs)
