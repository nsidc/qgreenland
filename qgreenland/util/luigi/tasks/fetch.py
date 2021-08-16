import os
import shutil

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import ASSETS_DIR, PRIVATE_ARCHIVE_DIR, TaskType
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

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop,
        )

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


class FetchManualDataFiles(FetchTask):
    def run(self):
        local_dir = os.path.join(PRIVATE_ARCHIVE_DIR, self.dataset_cfg.id)
        with temporary_path_dir(self.output()) as temp_path:
            shutil.copytree(local_dir, temp_path, dirs_exist_ok=True)


class FetchRepoDataFiles(FetchTask):
    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            source_path = self.asset_cfg.filepath
            out_path = Path(temp_path) / self.asset_cfg.filepath.name

            shutil.copy2(source_path, out_path)

class FetchOgrRemoteData(FetchTask):
    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            url = self.asset_cfg.query_url

            ofile = os.path.join(temp_path, 'fetched.geojson')
            ogr2ogr_kwargs = {
                'oo': 'FEATURE_SERVER_PAGING=YES',
            }

            ogr2ogr(f'"{url}"', ofile, **ogr2ogr_kwargs)
