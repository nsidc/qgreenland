import os
import shutil

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import LOCALDATA_DIR, PRIVATE_ARCHIVE_DIR, TaskType
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.misc import (
    datasource_dirname,
    fetch_and_write_file,
    temporary_path_dir,
)
from qgreenland.util.vector import ogr2ogr


# TODO: call this 'FetchDataset'? 'FetchAsset'?
class FetchTask(luigi.Task):
    dataset_id = luigi.Parameter()
    asset_id = luigi.Parameter()

    @property
    def output_name(self):
        return datasource_dirname(
            dataset_id=self.dataset_cfg.id,
            asset_id=self.asset_cfg.id,
        )

    @property
    def dataset_cfg(self):
        return CONFIG.datasets[self.dataset_id]

    @property
    def asset_cfg(self):
        return self.dataset_cfg.assets[self.asset_id]


class FetchCmrGranule(FetchTask):
    session = None

    def output(self):
        path = [TaskType.FETCH.value, self.output_name]
        return luigi.LocalTarget(os.path.join(*path))

    def run(self):
        granule = get_cmr_granule(
            granule_ur=self.asset_cfg.granule_ur,
            collection_concept_id=self.asset_cfg.collection_concept_id)

        verify = self.asset_cfg.verify
        if verify is not None:
            raise RuntimeError(
                'Ignoring TLS certificate verification is not supported for CMR'
                ' granules.',
            )

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
            format=luigi.format.Nop,
        )

    def run(self):
        if self.asset_cfg.type == 'cmr':
            raise RuntimeError('Use a FetchCmrGranule task!')

        with temporary_path_dir(self.output()) as temp_path:
            for url in self.asset_cfg['http']['urls']:
                fetch_and_write_file(
                    url,
                    output_dir=temp_path,
                    verify=self.asset_cfg.verify,
                )


class FetchLocalDataFiles(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop,
        )

    def run(self):
        if self.dataset_cfg['access_method'] == 'local':
            local_dir = LOCALDATA_DIR
            with temporary_path_dir(self.output()) as temp_path:
                for filename in self.source_cfg['urls']:
                    source_path = os.path.join(local_dir, filename)
                    out_path = os.path.join(temp_path, os.path.basename(filename))

                    shutil.copy2(source_path, out_path)

        elif self.dataset_cfg['access_method'] == 'manual':
            local_dir = os.path.join(PRIVATE_ARCHIVE_DIR, self.dataset_cfg['id'])
            with temporary_path_dir(self.output()) as temp_path:
                shutil.copytree(local_dir, temp_path, dirs_exist_ok=True)

        else:
            raise RuntimeError(
                'You selected an unsupported access_method:'
                f' {self.dataset_cfg["access_method"]}',
            )


class FetchOgrRemoteData(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop,
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            url = self.source_cfg['query_url']

            ofile = os.path.join(temp_path, 'fetched.geojson')
            ogr2ogr_kwargs = {
                'oo': 'FEATURE_SERVER_PAGING=YES',
            }

            ogr2ogr(f'"{url}"', ofile, **ogr2ogr_kwargs)
