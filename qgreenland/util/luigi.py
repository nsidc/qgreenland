import os

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.misc import get_layer_config, get_layer_fs_path


class LayerConfigMixin(luigi.Task):
    """Allow tasks to receive layer_id as parameter and get the correct config.

    Used for all tasks that require a layer config. This way, we only have to
    pass a string instead of a whole config object as a parameter.
    """

    layer_id = luigi.Parameter()
    task_type = None

    @property
    def layer_cfg(self):
        return get_layer_config(self.layer_id)

    @property
    def short_name(self):
        return self.layer_cfg['short_name']

    @property
    def outdir(self):
        if self.task_type not in TaskType:
            msg = (f"This class defines self.task_type as '{self.task_type}'. "
                   f'Must be one of: {list(TaskType)}.')
            raise RuntimeError(msg)

        if self.task_type is TaskType.FINAL:
            outdir = (f"{TaskType.FINAL.value}/{self.layer_cfg['layer_group']}/"
                      f'{self.short_name}')
        else:
            outdir = f'{self.task_type.value}/{self.short_name}'

        os.makedirs(outdir, exist_ok=True)
        return outdir


class LayerTask(luigi.Task):
    """Allow top-level layer tasks to lookup config from class attr layer_id.

    Also standardizes output directory for top-level layer tasks.
    """

    def output(self):
        return luigi.LocalTarget(
            os.path.dirname(
                get_layer_fs_path(self.layer_id,
                                  self.cfg)
            )
        )

    @property
    def cfg(self):
        return get_layer_config(self.layer_id)
