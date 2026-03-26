import hashlib
import shutil
from pathlib import Path

import earthaccess
import luigi

from qgreenland.constants.paths import FETCH_DATASETS_DIR, PRIVATE_ARCHIVE_DIR
from qgreenland.models.config.asset import (
    CmrAsset,
    HttpAsset,
    ManualAsset,
    RepositoryAsset,
)
from qgreenland.util.command import interpolate_args, run_qgr_command
from qgreenland.util.config.config import get_config
from qgreenland.util.layer import datasource_dirname
from qgreenland.util.luigi.target import temporary_path_dir
from qgreenland.util.request import fetch_and_write_file


# TODO: call this 'FetchDataset'? 'FetchAsset'?
class FetchTask(luigi.Task):
    dataset_id: str = luigi.Parameter()
    asset_id: str = luigi.Parameter()

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
            raise RuntimeError(f"Expected CMR asset. Received: {self.asset_cfg}")

        # earthaccess expects envvars `EARTHDATA_USERNAME` and
        # `EARTHDATA_PASSWORD`.
        earthaccess.login(strategy="environment")

        granules = earthaccess.search_data(
            granule_ur=self.asset_cfg.granule_ur,
            collection_concept_id=self.asset_cfg.collection_concept_id,
        )
        if len(granules) != 1:
            raise RuntimeError(
                f"Expected exactly one granule, received: {granules}",
            )

        with temporary_path_dir(self.output()) as temp_path:
            files = earthaccess.download(granules, str(temp_path))
            if not files:
                raise RuntimeError(
                    f"Unexpected problem downloading {granules}.\n"
                    "This may mean that Earthdata Login (EDL) is not working!"
                )


class FetchDataFiles(FetchTask):
    def output(self):
        return luigi.LocalTarget(
            FETCH_DATASETS_DIR / self.output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        if type(self.asset_cfg) is not HttpAsset:
            raise RuntimeError(f"Expected HTTP asset. Received: {self.asset_cfg}")

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
                "You selected an unsupported access_method:" f" {type(self.asset_cfg)}",
            )


class FetchDataWithCommand(FetchTask):
    """Fetch data using a command, writing to '{output_dir}'."""

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


class MergeFetchedDataTask(luigi.Task):
    """Merge, if necessary, fetched data from multiple inputs into a single directory.

    `requires_fetch_tasks` takes a list of fetch tasks.

    If provided with a list of len 1, this task is a no-op.

    If the list has multiple fetch tasks, it merges them into a single output
    directory via symlinks for use in layer steps (each layer step is expected
    to get a single input_dir).

    NOTE/TODO: This task does not handle conflicts between multiple input
    sources. It is expected that each fetched input source will have a distinct
    filenames.

    Useful when wanting to combine multiple datasets into one layer!
    """

    requires_fetch_tasks = luigi.Parameter()

    def requires(self):
        """Dynamically specify tasks this task depends on."""
        return self.requires_fetch_tasks

    def output(self):
        # If there's just one task here, we keep the output as-is. No need to
        # merge anything.
        if len(self.requires_fetch_tasks) == 1:
            return self.requires_fetch_tasks[0].output()

        # Join the dirnames together
        joined_output_name = "-".join(
            datasource_dirname(dataset_id=task.dataset_id, asset_id=task.asset_id)
            for task in self.requires_fetch_tasks
        )
        # TODO: update output name ot include at least some of the source
        # datasets? Or think about some other mechanism to cleanup this when
        # source data are removed?
        output_name = hashlib.md5(joined_output_name.encode("utf-8")).hexdigest()
        return luigi.LocalTarget(
            FETCH_DATASETS_DIR / output_name,
            format=luigi.format.Nop,
        )

    def run(self):
        """Symlink source datasets into a common directory for use in layer steps."""
        with temporary_path_dir(self.output()) as temp_path:
            for required_fetch_task in self.requires_fetch_tasks:
                output_path = required_fetch_task.output().path
                for item in Path(output_path).iterdir():
                    if not item.is_file():
                        continue

                    new_output = Path(temp_path) / item.relative_to(output_path)
                    new_output.parent.mkdir(parents=True, exist_ok=True)
                    new_output.symlink_to(item)
