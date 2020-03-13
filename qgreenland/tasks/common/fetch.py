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


class FetchDataFiles(luigi.Task):
    source_cfg = luigi.DictParameter()
    output_name = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(
            os.path.join(TaskType.FETCH.value,
                         self.output_name),
            format=luigi.format.Nop
        )

    def run(self):
        if 'cmr' in self.source_cfg:
            raise RuntimeError('Use a FetchCmrGranule task!')

        with temporary_path_dir(self.output()) as temp_path:
            for url in self.source_cfg['urls']:
                resp = fetch_file(url)

                url_slash_index = resp.url.rfind('/')
                fn = resp.url[url_slash_index + 1:]
                fp = os.path.join(temp_path, fn)

                with open(fp, 'wb') as f:
                    f.write(resp.content)
