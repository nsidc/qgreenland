"""Responsible for task orchestration.

Manages input and output directories and various ways of running pipeline steps.
Doesn't care about what files end up in the output directory, that's the
responsibility of the step configuration.
"""
import shutil
from pathlib import Path

import luigi

from qgreenland.constants.paths import WIP_DIR
from qgreenland.models.config.step import AnyStep
from qgreenland.runners import step_runner
from qgreenland.util.config.config import get_config
from qgreenland.util.layer import (
    get_layer_compile_dir,
    get_layer_fp,
    get_layer_release_dir,
)
from qgreenland.util.luigi.target import temporary_path_dir
from qgreenland.util.tree import leaf_lookup


class QgrLayerTask(luigi.Task):
    requires_task = luigi.Parameter()
    layer_id = luigi.Parameter()

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id})'
        )

    def requires(self):
        """Dynamically specify task this task depends on."""
        return self.requires_task

    @property
    def layer_cfg(self):
        """Find the config associated with this layer."""
        config = get_config()
        return config.layers[self.layer_id]

    @property
    def node(self):
        """Find the corresponding LayerNode in the config tree."""
        config = get_config()
        return leaf_lookup(config.layer_tree, target_node_name=self.layer_id)


# TODO: Rename... QgrTask? ChainableLayerTask? ChainableLayerStep?
# LayerStepTask?
class ChainableTask(QgrLayerTask):
    """Define dependencies at instantiation-time.

    Each chainable task is specific to a single step in creation of a single
    layer (for now).

    TODO: Consider multiple inheritance to separate layer/step repsonsibility
    from dependency-specification responsibility?
    """

    step_number = luigi.IntParameter()

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id},'
            f' step_number={self.step_number})'
        )

    @property
    def step(self):
        return self.layer_cfg.steps[self.step_number]

    @property
    def step_identifier(self):
        """Generate a short string uniquely identifying a step within a layer.

        WARNING: Only uniquely identifies a _step_ in the context of a layer;
        does not uniquely ID a step + layer combination.
        """
        return f'{self.step_number:02}-{self.step.type}-{self.step.id}'

    def output(self):
        """Define a directory for the step's behavior to write things into.

        We don't care what those files are or what directory structure lies
        within.

        NOTE: As soon as this directory exists, Luigi will consider this Task
        complete. _Always_ wrap behaviors in a temporary directory for outputs.
        """
        return luigi.LocalTarget(WIP_DIR / self.layer_id / self.step_identifier)

    def run(self):
        """Execute the step with a temporary directory.

        Enables Luigi to trigger the next job at the right time.

        NOTE: If jobs fail, temporary directory is not cleaned up. The WIP dir
        is ephemeral and will be cleaned up in a more wholesale manner.
        """
        with temporary_path_dir(self.output()) as temp_path:
            step_runner(
                self.step,
                input_dir=self.input().path,
                output_dir=str(temp_path),
            )


class LinkLayer(QgrLayerTask):

    def output(self):
        return luigi.LocalTarget(
            get_layer_compile_dir(self.node),
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            for inp in Path(self.input().path).glob('*'):
                # Hard link final layer files to the zip compile directory.
                #
                # NOTE: Hardlink API is backwards to the symlink API...
                # https://docs.python.org/3/library/pathlib.html#pathlib.Path.link_to
                inp.link_to(temp_path / inp.name)


class FinalizeTask(QgrLayerTask):
    """Move layer to the layer hosting/release location and add metadata files.

    provenance.txt: What steps were done to create this final layer file?

    TODO: metadata.txt or metadata.json containing layer/dataset metadata?
    """

    def output(self):
        return luigi.LocalTarget(
            get_layer_release_dir(self.node),
        )

    def run(self):
        # TODO: Separate "put in layer release dir" from "symlink to compile
        # dir"?
        input_path = Path(self.input().path)
        if not input_path.is_dir():
            raise RuntimeError(
                'Expected final output to be a directory. Received:'
                f' {input_path}!',
            )

        # Find compatible layer in dir (gpkg | tif). We only expect one file to
        # exist in the final layer dir.
        input_fp = get_layer_fp(input_path)

        # Copy file in there, renaming after layer id.
        final_fn = f'{self.layer_cfg.id}{input_fp.suffix}'
        with temporary_path_dir(self.output()) as temp_path:
            shutil.copy2(input_fp, temp_path / final_fn)

            # Create layer provenance file. This is not an "AncillaryFile" job
            # because we need one file per layer.
            with open(temp_path / 'provenance.txt', 'w') as provenance_file:
                provenance_file.write(
                    steps_to_provenance_text(self.layer_cfg.steps),
                )


def steps_to_provenance_text(steps: list[AnyStep]) -> str:
    steps_as_text = [step.provenance for step in steps]

    return '\n\n'.join(steps_as_text)
