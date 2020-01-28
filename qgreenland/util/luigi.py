import os

import luigi

from qgreenland.constants import DATA_DIR, DATA_FINAL_DIR, TaskType


class LayerConfigMixin(luigi.Task):
    layer_cfg = luigi.DictParameter()
    task_type = None

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
            outdir = (f"{DATA_FINAL_DIR}/{self.layer_cfg['layer_group']}/"
                      f'{self.short_name}')
        else:
            outdir = f'{DATA_DIR}/{self.task_type.value}/{self.short_name}'

        os.makedirs(outdir, exist_ok=True)
        return outdir
