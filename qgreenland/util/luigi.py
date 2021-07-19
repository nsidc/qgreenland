import os
import shutil
from typing import Optional

import luigi

from qgreenland.config import CONFIG
from qgreenland.constants import TaskType
from qgreenland.util.misc import get_layer_dir, get_layer_fn, temporary_path_dir


# TODO: QgrTask?
class ChainableTask(luigi.Task):
    requires_task = luigi.Parameter()
    layer_id = luigi.Parameter()

    def requires(self):
        return self.requires_task

    # TODO: return a deepcopy of these properties.
    @property
    def layer_cfg(self):
        return CONFIG['layers'][self.layer_id]

    @property
    def id(self):
        return self.layer_cfg['id']

    @property
    def outdir(self):
        # We could possibly DRY this out by adding a task_type param to
        # get_layer_path
        if self.task_type not in TaskType:
            msg = (f"This class defines self.task_type as '{self.task_type}'. "
                   f'Must be one of: {list(TaskType)}.')
            raise RuntimeError(msg)

        if self.task_type is TaskType.FINAL:
            outdir = (f"{TaskType.FINAL.value}/{self.layer_cfg['layer_group']}/"
                      f'{self.id}')
        else:
            outdir = f'{self.task_type.value}/{self.id}'

        os.makedirs(outdir, exist_ok=True)
        return outdir


class LayerStepTask(ChainableTask):
    """A chainable Luigi task which runs the given configured processing step."""
    step_number = luigi.IntParameter()

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id})'
        )

    def run(self):
        """Select a runner based on the step configuration and run the step."""

        # task = RUNNERS[task_type](
        #     task_params,
        #     required_task=task,
        #     layer_id=layer_id,
        # )

    def output(self):
        """How do we know what the output is?

        There could be multiple files and/or file types? There are steps where
        we use ogr2ogr to e.g., convert a shapefile to a gpkg. The previous
        task's output determines the next task's input.

        Maybe some "smart" routine could infer the correct output from the
        available set of files after running."""
        pass



# we need a way to create tasks that require other tasks without having to create a new class.

# could this be a function that takes some args and just returns a Luigi Task?

# what other features does the old layer task have that we might need?

# Maybe instead of 'LayerTask' (or in addition, inheriting from) create
# CommandTask, PythonTask, TemplateTask

# TODO: rename to 'ChainableTask'? 'ChainableLayerStep'?
class LayerTask(luigi.Task):
    """Chainable task allows dynamic dependency specification at instantiation.

    Allow tasks to receive layer_id as parameter and get the correct config.

    Used for all tasks that require a layer config. This way, we only have to
    pass a string instead of a whole config object as a parameter.
    """

    requires_task = luigi.Parameter()
    layer_id = luigi.Parameter()
    task_type: Optional[TaskType] = None

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id})'
        )

    def requires(self):
        return self.requires_task

    # TODO: return a deepcopy of these properties.
    @property
    def layer_cfg(self):
        return CONFIG['layers'][self.layer_id]

    @property
    def id(self):
        return self.layer_cfg['id']

    @property
    def filename(self):
        return get_layer_fn(self.layer_cfg)

    @property
    def outdir(self):
        # We could possibly DRY this out by adding a task_type param to
        # get_layer_path
        if self.task_type not in TaskType:
            msg = (f"This class defines self.task_type as '{self.task_type}'. "
                   f'Must be one of: {list(TaskType)}.')
            raise RuntimeError(msg)

        if self.task_type is TaskType.FINAL:
            outdir = (f"{TaskType.FINAL.value}/{self.layer_cfg['layer_group']}/"
                      f'{self.id}')
        else:
            outdir = f'{self.task_type.value}/{self.id}'

        os.makedirs(outdir, exist_ok=True)
        return outdir

    # TODO: Standardize the output method of layer tasks
    # def output(self):

class Finalize(LayerTask):
    """Allow top-level layer tasks to lookup config from class attr layer_id.

    Also standardizes output directory for top-level layer tasks.
    """

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id})'
        )

    @property
    def cfg(self):
        return CONFIG['layers'][self.layer_id]

    def output(self):
        return luigi.LocalTarget(get_layer_dir(self.cfg))

    def run(self):
        if os.path.isdir(self.input().path):
            source_path = self.input().path
        else:
            source_path = os.path.dirname(self.input().path)

        with temporary_path_dir(self.output()) as temp_path:
            shutil.copytree(source_path, temp_path, dirs_exist_ok=True)


# TODO: can probably remove this!?
class LayerPipeline(luigi.Task):
    """Allow top-level layer tasks to lookup config from class attr layer_id.

    Also standardizes output directory for top-level layer tasks.
    """

    layer_id = luigi.Parameter()

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'layer_id={self.layer_id})'
        )

    @property
    def cfg(self):
        return CONFIG['layers'][self.layer_id]

    def output(self):
        return luigi.LocalTarget(get_layer_dir(self.cfg))

    def run(self):
        if os.path.isdir(self.input().path):
            source_path = self.input().path
        else:
            source_path = os.path.dirname(self.input().path)

        with temporary_path_dir(self.output()) as temp_path:
            shutil.copytree(source_path, temp_path, dirs_exist_ok=True)
