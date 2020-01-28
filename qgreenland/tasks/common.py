"""common.py: Tasks that could apply to any type of dataproduct."""
import os

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.luigi import LayerConfigMixin
from qgreenland.util.misc import fetch_file


class FetchData(LayerConfigMixin, luigi.Task):
    task_type = TaskType.FETCH

    def output(self):
        # luigi.format.Nop is required to write binary file.
        # https://github.com/spotify/luigi/issues/1647
        of = os.path.join(self.outdir, f'{self.short_name}.data')
        return luigi.LocalTarget(of, format=luigi.format.Nop)

    def run(self):
        resp = fetch_file(self.layer_cfg['source']['url'])
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)
