"""layers.py: Top-level tasks for generating layers from dataproducts.

All tasks in this file should read configuration from layers.yml.
"""
import os

import luigi

from qgreenland.tasks.common import ExtractNcDataset, FetchData
from qgreenland.tasks.raster import BuildRasterOverviews, ReprojectRaster, SubsetRaster
from qgreenland.tasks.shapefile import (ReprojectShapefile,
                                        SubsetShapefile,
                                        UnzipShapefile)
from qgreenland.util.misc import (load_layer_config,
                                  get_layer_fs_path,
                                  temporary_path_dir)
from qgreenland.util.shapefile import find_shapefile_in_dir


class LayerTaskMixin(luigi.Task):

    def output(self):
        return luigi.LocalTarget(
            os.path.dirname(
                get_layer_fs_path(self.layer_name,
                                  self.cfg)
            )
        )


# TODO: Consider creating a mixin or something for reading yaml config to
# DRY out the code for layer classes
# e.g. use a class attribute to automatically load config:
#   layername = 'coastlines'
class Coastlines(LayerTaskMixin, luigi.Task):
    """Rename files to their final location."""

    layer_name = 'coastlines'
    cfg = load_layer_config(layer_name)

    def requires(self):
        fetch_data = FetchData(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['short_name']
        )  # ->
        unzip_shapefile = UnzipShapefile(
            requires_task=fetch_data,
            layer_cfg=self.cfg
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=unzip_shapefile,
            layer_cfg=self.cfg
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_cfg=self.cfg
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


class ArcticDEM(LayerTaskMixin, luigi.Task):
    """Rename files to their final location."""

    layer_name = 'arctic_dem'
    cfg = load_layer_config(layer_name)

    def requires(self):
        fetch_data = FetchData(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['short_name']
        )  # ->
        reproject_raster = ReprojectRaster(
            requires_task=fetch_data,
            layer_cfg=self.cfg
        )  # ->
        subset_raster = SubsetRaster(
            requires_task=reproject_raster,
            layer_cfg=self.cfg
        )  # ->
        return BuildRasterOverviews(
            requires_task=subset_raster,
            layer_cfg=self.cfg
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_name}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)


class BedMachineDataset(LayerTaskMixin, luigi.Task):
    """Dataproduct IDBMG4.

    https://nsidc.org/data/IDBMG4
    """

    dataset_name = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layer_name = f'bedmachine_{self.dataset_name}'
        self.cfg = load_layer_config(self.layer_name)

    def requires(self):
        output_name = self.cfg['source'].get('name', self.cfg['short_name'])

        fetch_data = FetchData(
            source_cfg=self.cfg['source'],
            output_name=output_name
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_cfg=self.cfg,
            dataset_name=self.dataset_name
        )  # ->
        return ReprojectRaster(
            requires_task=extract_nc_dataset,
            layer_cfg=self.cfg,
        )

    def run(self):
        with temporary_path_dir(self.output()) as temp_path:
            new_fp = os.path.join(
                temp_path,
                f"{self.layer_name}.{self.cfg['file_type']}"
            )

            os.rename(self.input().path, new_fp)
