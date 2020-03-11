import os

import luigi

from qgreenland.constants import CONFIG, TaskType
from qgreenland.util.misc import get_layer_dir, get_layer_fn


# TODO: Rename to LayerTask
class LayerConfigMixin(luigi.Task):
    """Allow tasks to receive layer_id as parameter and get the correct config.

    Used for all tasks that require a layer config. This way, we only have to
    pass a string instead of a whole config object as a parameter.
    """

    layer_id = luigi.Parameter()
    task_type = None

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
        # get_layer_fs_path
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


class LayerPipeline(luigi.Task):
    """Allow top-level layer tasks to lookup config from class attr layer_id.

    Also standardizes output directory for top-level layer tasks.
    """

    layer_id = luigi.Parameter()

    @property
    def cfg(self):
        return CONFIG['layers'][self.layer_id]

    def output(self):
        return luigi.LocalTarget(get_layer_dir(self.cfg))
