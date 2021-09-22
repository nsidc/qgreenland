import os
import shutil
from pathlib import Path

import luigi

from qgreenland.constants import PRIVATE_ARCHIVE_DIR, PROJECT_DIR, TaskType
from qgreenland.models.config.asset import (
    ConfigDatasetCmrAsset,
    ConfigDatasetHttpAsset,
    ConfigDatasetManualAsset,
    ConfigDatasetRepositoryAsset,
)
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.config.config import CONFIG
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
        if type(self.asset_cfg) is not ConfigDatasetCmrAsset:
            raise RuntimeError(f'Expected CMR asset. Received: {self.asset_cfg}')

        granule = get_cmr_granule(
            granule_ur=self.asset_cfg.granule_ur,
            collection_concept_id=self.asset_cfg.collection_concept_id)

        with temporary_path_dir(self.output()) as temp_path:
            for url in granule.urls:
                if not self.session:
                    self.session = make_session(hosts=[url], verify=True)

                fetch_and_write_file(
                    url,
                    output_dir=temp_path,
                    session=self.session,
                )


class FetchDataFiles(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop,
        )

    def run(self):
        if type(self.asset_cfg) is not ConfigDatasetHttpAsset:
            raise RuntimeError(f'Expected HTTP asset. Received: {self.asset_cfg}')

        with temporary_path_dir(self.output()) as temp_path:
            for url in self.asset_cfg.urls:
                fetch_and_write_file(
                    url,
                    output_dir=temp_path,
                    verify=self.asset_cfg.verify_tls,
                )


class FetchLocalDataFiles(FetchTask):
    """Fetch data that's already on the local installation.

    e.g. "Manual" assets which are downloaded by humans, "Repository" assets
    which are present in this git repo.
    """

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop,
        )

    def run(self):
        if isinstance(self.asset_cfg, ConfigDatasetRepositoryAsset):
            with temporary_path_dir(self.output()) as temp_path:
                # TODO: Why doesn't the typchecker catch if we were to access
                # `self.asset_cfg.urls` here? That's not available on a
                # ConfigDatasetRepositoryAsset. Encountered a runtime error when
                # it should have been a type error.

                out_path = Path(temp_path) / self.asset_cfg.filepath.name
                shutil.copy2(
                    PROJECT_DIR / self.asset_cfg.filepath,
                    out_path,
                )

        elif isinstance(self.asset_cfg, ConfigDatasetManualAsset):
            local_dir = os.path.join(PRIVATE_ARCHIVE_DIR, self.dataset_cfg.id)
            with temporary_path_dir(self.output()) as temp_path:
                shutil.copytree(local_dir, temp_path, dirs_exist_ok=True)

        else:
            raise RuntimeError(
                'You selected an unsupported access_method:'
                f' {type(self.asset_cfg)}',
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
            url = self.asset_cfg.query_url

            ofile = os.path.join(temp_path, 'fetched.geojson')
            ogr2ogr_kwargs = {
                'oo': 'FEATURE_SERVER_PAGING=YES',
            }

            ogr2ogr(f'"{url}"', ofile, **ogr2ogr_kwargs)
