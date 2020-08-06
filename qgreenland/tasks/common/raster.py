import os
import shutil

import luigi
import rasterio as rio

from qgreenland.constants import PROJECT_EXTENT, TaskType
from qgreenland.util.luigi import LayerTask
from qgreenland.util.misc import find_single_file_by_ext, temporary_path_dir
from qgreenland.util.raster import warp_raster


class BuildRasterOverviews(LayerTask):
    task_type = TaskType.WIP

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'overviews'))

    def run(self):
        # TODO: Extract this to LayerTask as a property?
        # TODO: Find in dir by self.filename instead? Wouldn't work if the
        #       upstream task was e.g. unzip
        ifile = find_single_file_by_ext(self.input().path,
                                        ext=self.layer_cfg['file_type'])

        overviews_kwargs = {
            'overview_levels': (2, 4, 8, 16),
            'resampling_method': 'average'
        }

        overviews_kwargs.update(
            self.layer_cfg.get('overviews_kwargs', {})
        )

        overview_levels = overviews_kwargs['overview_levels']
        resampling_str = overviews_kwargs['resampling_method']

        try:
            resampling_method = rio.enums.Resampling[resampling_str]
        except KeyError:
            raise RuntimeError(
                f"'{resampling_str}' is not a valid resampling method."
            )

        with temporary_path_dir(self.output()) as tmp_dir:
            tmp_path = os.path.join(tmp_dir, self.filename)
            # Copy the existing file into place. Currently, this task creates
            # 'internal overviews', which changes the file itself.
            shutil.copy2(ifile, tmp_path)

            with rio.open(tmp_path, 'r+') as ds:
                ds.build_overviews(overview_levels, resampling_method)


class WarpRaster(LayerTask):
    task_type = TaskType.WIP
    input_ext_override = luigi.Parameter(default=None)

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'reproject'))

    def run(self):
        if 'override_source_projection' in self.layer_cfg:
            # But we can still pass in warp_kwargs to set source projection...
            raise NotImplementedError(
                'override_source_projection not implemented for raster layers.'
            )

        warp_kwargs = {
            'resampleAlg': 'bilinear',
            'outputBounds': list(PROJECT_EXTENT.values())
        }
        if 'warp_kwargs' in self.layer_cfg:
            warp_kwargs.update(self.layer_cfg['warp_kwargs'])

        file_ext = self.input_ext_override or self.layer_cfg['file_type']
        inp_path = find_single_file_by_ext(self.input().path, ext=file_ext)

        with temporary_path_dir(self.output()) as tmp_dir:
            out_path = os.path.join(tmp_dir, self.filename)
            warp_raster(inp_path, out_path,
                        layer_cfg=self.layer_cfg,
                        warp_kwargs=warp_kwargs)
