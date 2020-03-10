import os

import luigi

from qgreenland.constants import TaskType
from qgreenland.util.cmr import get_cmr_granule
from qgreenland.util.edl import create_earthdata_authenticated_session as make_session
from qgreenland.util.misc import fetch_file, temporary_path_dir


class FetchCmrGranule(luigi.Task):
    source_cfg = luigi.DictParameter()
    output_name = luigi.Parameter()

    session = None

    def output(self):
        path = [TaskType.FETCH.value, self.output_name]
        if 'subdir_path' in self.source_cfg:
            path.append(self.source_cfg['subdir_path'])

        return luigi.LocalTarget(os.path.join(*path))

    def run(self):
        granule = get_cmr_granule(granule_ur=self.source_cfg['granule_ur'])

        with temporary_path_dir(self.output()) as temp_path:
            for url in granule.urls:
                if not self.session:
                    self.session = make_session(hosts=[url])

                fn = os.path.basename(url)
                fp = os.path.join(temp_path, fn)

                resp = fetch_file(url, session=self.session)
                with open(fp, 'wb') as f:
                    f.write(resp.content)


class FetchDataFile(luigi.Task):
    source_cfg = luigi.DictParameter()
    output_name = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name,
                         f'{self.output_name}.data'),
            format=luigi.format.Nop
        )

    def run(self):
        if 'cmr' in self.source_cfg:
            raise RuntimeError('Use a FetchCmrGranule task!')

        if len(self.source_cfg['urls']) > 1:
            raise NotImplementedError('No Task implemented for handling >1 source url')

        # TODO: We can more-or-less reuse this code, but iterate over "urls".
        url = self.source_cfg['urls'][0]

        resp = fetch_file(url)
        with self.output().open('wb') as outfile:
            outfile.write(resp.content)
