"""common.py: Tasks that could apply to any type of dataproduct."""

import luigi

from qgreenland.constants import DATA_WIP_DIR
from qgreenland.util import fetch_file


class FetchData(luigi.Task):
    layer_cfg = luigi.Parameter()

    def output(self):
        # luigi.format.Nop is required to write binary file.
        # https://github.com/spotify/luigi/issues/1647

        # TODO: Stop assuming the extension. Could be zip, hdf, etc.
        fn = self.layer_cfg['short_name']
        return luigi.LocalTarget(f'{DATA_WIP_DIR}/{fn}.zip',
                                 format=luigi.format.Nop)

    def run(self):
        resp = fetch_file(self.layer_cfg['source']['url'])
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)
