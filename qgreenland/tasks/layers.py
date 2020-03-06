"""layers.py: Top-level tasks for generating layers from dataproducts.

All tasks in this file should read configuration from layers.yml.
"""
import os

import luigi

from qgreenland.tasks.common import ExtractNcDataset, FetchDataFile, FetchCmrGranule
from qgreenland.tasks.raster import BuildRasterOverviews, ReprojectRaster, SubsetRaster
from qgreenland.tasks.shapefile import (ReprojectShapefile,
                                        SubsetShapefile,
                                        UnzipShapefile)
from qgreenland.util.misc import (get_layer_config,
                                  get_layer_fs_path,
                                  temporary_path_dir)
from qgreenland.util.shapefile import find_shapefile_in_dir


class LayerTask(luigi.Task):

    def output(self):
        return luigi.LocalTarget(
            os.path.dirname(
                get_layer_fs_path(self.layer_name,
                                  self.cfg)
            )
        )

    @property
    def cfg(self):
        return get_layer_config(self.layer_name)


# TODO: Consider creating a mixin or something for reading yaml config to
# DRY out the code for layer classes
# e.g. use a class attribute to automatically load config:
#   layername = 'coastlines'
class Coastlines(LayerTask):
    """Rename files to their final location."""

    layer_name = 'coastlines'

    def requires(self):
        fetch_data = FetchDataFile(
            # TODO: Make this in to a for loop over `sources`
            source_cfg=self.cfg['sources'][0],
            output_name=self.cfg['short_name']
        )  # ->
        unzip_shapefile = UnzipShapefile(
            requires_task=fetch_data,
            layer_name=self.layer_name
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=unzip_shapefile,
            layer_name=self.layer_name
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_name=self.layer_name
        )

    def run(self):
        shapefile = find_shapefile_in_dir(self.input().path)
        processed_shapefile_dir = os.path.dirname(shapefile)

        with temporary_path_dir(self.output()) as temp_path:
            for f in os.listdir(processed_shapefile_dir):
                _, ext = f.split('.')
                old_fp = os.path.join(processed_shapefile_dir, f)
                new_fp = os.path.join(
                    temp_path,
                    f'{self.layer_name}.{ext}')

                os.rename(old_fp, new_fp)


class ArcticDEM(LayerTask):
    """Rename files to their final location."""

    layer_name = 'arctic_dem'

    def requires(self):
        fetch_data = FetchDataFile(
            source_cfg=self.cfg['sources'][0],
            output_name=self.cfg['short_name']
        )  # ->
        reproject_raster = ReprojectRaster(
            requires_task=fetch_data,
            layer_name=self.layer_name
        )  # ->
        subset_raster = SubsetRaster(
            requires_task=reproject_raster,
            layer_name=self.layer_name
        )  # ->
        return BuildRasterOverviews(
            requires_task=subset_raster,
            layer_name=self.layer_name
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_name}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)


class BedMachineDataset(LayerTask):
    """Dataproduct IDBMG4.

    This is a NetCDF dataproduct with many distinct datasets representing
    distinct measurements.

    https://nsidc.org/data/IDBMG4
    """

    dataset_name = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_name = f'bedmachine_{self.dataset_name}'

    def requires(self):
        source = self.cfg['sources'][0]
        output_name = source.get('name', self.cfg['short_name'])

        fetch_data = FetchCmrGranule(
            source_cfg=source,
            output_name='bedmachine'
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_name=self.layer_name,
            dataset_name=self.dataset_name
        )  # ->
        return ReprojectRaster(
            requires_task=extract_nc_dataset,
            layer_name=self.layer_name
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_name}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)


class GlacierTerminus(LayerTask):
    """Dataproduct NSIDC-0642.

    https://nsidc.org/data/NSIDC-0642
    """

    layer_name = 'glacier_terminus'

    def requires(self):
        for source in self.cfg['sources']:
            fetch_data = FetchCmrGranule(source_cfg=source,
                                         output_name=self.cfg['short_name'])
            yield ReprojectShapefile(
                requires_task=fetch_data,
                layer_name=self.layer_name
            )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            for inp in self.input():
                # Move directories containing granules
                new_fp = os.path.join(temp_path, os.path.basename(inp.path))
                os.rename(inp.path, new_fp)
