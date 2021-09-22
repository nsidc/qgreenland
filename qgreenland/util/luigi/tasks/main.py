"""Responsible for task orchestration.

Manages input and output directories and various ways of running pipeline steps.
Doesn't care about what files end up in the output directory, that's the
responsibility of the step configuration.
"""
import shutil
from pathlib import Path

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import (
    RELEASES_LAYERS_DIR,
    TaskType,
)
from qgreenland.models.config.step import AnyStep
from qgreenland.runners import step_runner
from qgreenland.util.misc import get_final_layer_dir, get_layer_fp, temporary_path_dir
from qgreenland.util.tree import leaf_lookup


class QgrLayerTask(luigi.Task):
    # TODO: DRY
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
        return CONFIG.layers[self.layer_id]


# TODO: Rename... QgrTask? ChainableLayerTask? ChainableLayerStep?
class ChainableTask(QgrLayerTask):
    """Define dependencies at instantiation-time.

    Each chainable task is specific to a single step in creation of a single
    layer (for now).

    TODO: Consider multiple inheritance to separate layer/step repsonsibility
    from dependency-specification responsibility?
    """

    step_number = luigi.IntParameter()

    def __repr__(self):
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
        first_part = f'{self.step_number:02}-{self.step.type}'
        last_part = (
            f'-{self.step.args[0]}'
            if self.step.type == 'command'
            else 'TODO'
        )
        return f'{first_part}{last_part}'

    def output(self):
        """Define a directory for the step's behavior to write things into.

        We don't care what those files are or what directory structure lies
        within.

        NOTE: As soon as this directory exists, Luigi will consider this Task
        complete. _Always_ wrap behaviors in a temporary directory for outputs.
        """
        output_dir = (
            Path(TaskType.WIP.value)
            / self.layer_id
            / self.step_identifier
        )
        return luigi.LocalTarget(output_dir)

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
                output_dir=temp_path,
            )


class FinalizeTask(QgrLayerTask):
    """Allow top-level layer tasks to lookup config from class attr layer_id.

    Also standardizes output directory for top-level layer tasks.

    TODO: Expect a .gpkg or a .tif file in its input directory. If none (or >1?)
    exists, throw an exception so the pipeline developer knows. If one exists,
    create the appropriate type of QGIS Layer.

    TODO: How to handle "extra" layers that aren't in the zip, but are exposed
    for use with plugin? Separate "Final" step? Or make this one handle both
    cases?
    """

    @property
    def node(self):
        return leaf_lookup(CONFIG.layer_tree, target_node_name=self.layer_id)

    def output(self):
        return luigi.LocalTarget(
            get_final_layer_dir(self.node),
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

        # Recreate final layer release directory
        layer_final_dir = RELEASES_LAYERS_DIR / self.layer_cfg.id
        shutil.rmtree(layer_final_dir, ignore_errors=True)
        layer_final_dir.mkdir(parents=True)

        # Copy file in there, renaming after layer id.
        final_fn = f'{self.layer_cfg.id}{input_fp.suffix}'
        final_fp = layer_final_dir / final_fn
        shutil.copy2(input_fp, final_fp)

        # Create layer provenance file. This is not an "AncillaryFile" job
        # because we need one file per layer.
        with open(layer_final_dir / 'provenance.txt', 'w') as provenance_file:
            provenance_file.write(
                steps_to_provenance_text(self.layer_cfg.steps),
            )

        output_dir = Path(self.output().path)
        # Ensure output dir exists. The layer file symlink will go inside.
        output_dir.mkdir(parents=True, exist_ok=True)
        output_fn = output_dir / final_fn

        # Create a symbolic link to the final layer release directory inside the
        # zip compile directory.  Relative symlink allows it to work inside and
        # outside docker.
        # NOTE: Hardlink API is backwards to the symlink API...
        #    https://docs.python.org/3/library/pathlib.html#pathlib.Path.link_to
        final_fp.link_to(output_fn)


def steps_to_provenance_text(steps: list[AnyStep]) -> str:
    steps_as_text = [step.provenance for step in steps]

    return '\n\n'.join(steps_as_text)
