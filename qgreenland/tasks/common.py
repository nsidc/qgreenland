"""common.py: Tasks that could apply to any type of dataproduct."""

import luigi

from qgreenland.constants import DATA_DOWNLOAD_DIR
from qgreenland.util import fetch_file


class FetchData(luigi.Task):
    layer_cfg = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: Configure the extension. Could be zip, hdf, etc.
        short_name = self.layer_cfg['short_name']
        self.outfile = f'{DATA_DOWNLOAD_DIR}/{short_name}/{short_name}.data'

    def output(self):
        # luigi.format.Nop is required to write binary file.
        # https://github.com/spotify/luigi/issues/1647
        return luigi.LocalTarget(self.outfile, format=luigi.format.Nop)

    def run(self):
        resp = fetch_file(self.layer_cfg['source']['url'])
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)
