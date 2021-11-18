import shutil

import luigi

from qgreenland.constants.paths import (
    FETCH_DATASETS_DIR,
    PRIVATE_ARCHIVE_DIR,
)
from qgreenland.models.config.asset import (
    CmrAsset,
    HttpAsset,
    ManualAsset,
    RepositoryAsset,
)
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.command import interpolate_args, run_qgr_command
from qgreenland.util.config.config import get_config
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.layer import datasource_dirname
from qgreenland.util.luigi.target import temporary_path_dir
from qgreenland.util.request import fetch_and_write_file


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
        config = get_config()
        return config.datasets[self.dataset_id]

    @property
    def asset_cfg(self):
        return self.dataset_cfg.assets[self.asset_id]


class FetchCmrGranule(FetchTask):
    session = None

    def output(self):
        path = FETCH_DATASETS_DIR / self.output_name
        return luigi.LocalTarget(path)

    def run(self):
        if type(self.asset_cfg) is not CmrAsset:
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
            FETCH_DATASETS_DIR / self.output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        if type(self.asset_cfg) is not HttpAsset:
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
            FETCH_DATASETS_DIR / self.output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        if isinstance(self.asset_cfg, RepositoryAsset):

            with temporary_path_dir(self.output()) as temp_path:
                evaluated_filepath = self.asset_cfg.filepath.eval()

                out_path = temp_path / evaluated_filepath.name
                shutil.copy2(evaluated_filepath, out_path)

        elif isinstance(self.asset_cfg, ManualAsset):
            local_dir = PRIVATE_ARCHIVE_DIR / self.dataset_cfg.id
            with temporary_path_dir(self.output()) as temp_path:
                shutil.copytree(local_dir, temp_path, dirs_exist_ok=True)

        else:
            raise RuntimeError(
                'You selected an unsupported access_method:'
                f' {type(self.asset_cfg)}',
            )


class FetchDataWithCommand(FetchTask):
    """Fetch data using a command, writing to '{output_dir}'."""  # noqa: FS003

    def output(self):
        return luigi.LocalTarget(
            FETCH_DATASETS_DIR / self.output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            run_qgr_command(
                interpolate_args(
                    self.asset_cfg.args,
                    output_dir=temp_path,
                ),
            )


class FetchOgrRemoteData(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            FETCH_DATASETS_DIR / self.output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            url = self.asset_cfg.query_url

            ofile = temp_path / 'fetched.geojson'
            run_qgr_command(
                [
                    'ogr2ogr',
                    '-oo', 'FEATURE_SERVER_PAGING=YES',
                    str(ofile),
                    f'"{url}"',
                ],
            )
