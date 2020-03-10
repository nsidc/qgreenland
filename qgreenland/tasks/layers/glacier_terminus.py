import os

from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.shapefile import ReprojectShapefile
from qgreenland.util.luigi import LayerPipeline
from qgreenland.util.misc import temporary_path_dir


class GlacierTerminus(LayerPipeline):
    """Dataproduct NSIDC-0642.

    https://nsidc.org/data/NSIDC-0642
    """

    def requires(self):
        fetch_data = FetchCmrGranule(source_cfg=self.cfg['source'],
                                     output_name=self.cfg['id'])
        yield ReprojectShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            for inp in self.input():
                # Move directories containing granules
                new_fp = os.path.join(temp_path, os.path.basename(inp.path))
                os.rename(inp.path, new_fp)
