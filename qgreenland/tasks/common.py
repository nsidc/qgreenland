"""common.py: Tasks that could apply to any type of dataproduct."""
import os

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.cmr import granules_from_cmr
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
        layer_source = self.layer_cfg['source']
        if 'cmr' in layer_source:
            granules = granules_from_cmr(
                layer_source['cmr']['short_name'],
                layer_source['cmr']['version']
            )
            url = granules[0]['Online Access URLs']
        elif 'url' in layer_source:
            url = self.layer_cfg['source']['url']

        resp = fetch_file(url)
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)
