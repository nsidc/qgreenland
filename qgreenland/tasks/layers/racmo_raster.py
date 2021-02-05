import os

import luigi
import rasterio

from qgreenland.constants import TaskType
from qgreenland.exceptions import QgrRuntimeError
from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset, Unzip
from qgreenland.tasks.common.raster import (
    BuildRasterOverviews,
    GdalEdit,
    WarpRaster,
)
from qgreenland.util.luigi import LayerPipeline, LayerTask
from qgreenland.util.misc import (datasource_dirname,
                                  find_single_file_by_ext,
                                  temporary_path_dir)
from qgreenland.util.raster import apply_mask


class RacmoRaster(LayerPipeline):

    def requires(self):
        source = self.cfg['source']

        fetch_data = FetchLocalDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=unzip,
            layer_id=self.layer_id,
        )  # ->
        gdaledit = GdalEdit(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )
        warp_raster = WarpRaster(
            requires_task=gdaledit,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )


class ApplyPromiceMask(LayerTask):

    task_type = TaskType.WIP
    mask_fp = luigi.Parameter(default=None)

    def output(self):
        return luigi.LocalTarget(os.path.join(self.outdir, 'masked'))

    def run(self):
        inp_path = find_single_file_by_ext(self.input().path,
                                           ext=self.layer_cfg['file_type'])

        with rasterio.open(inp_path, 'r') as source_ds:
            source_data = source_ds.read(1)
            source_nodata = source_ds.nodata
            source_profile = source_ds.profile

        # TODO: better err msg
        if not source_nodata:
            raise QgrRuntimeError('Expected source DS with nodata.')

        with rasterio.open(self.mask_fp, 'r') as mask_ds:
            mask_data = mask_ds.read(1)

        # 3 = Greenland ice sheet; 2,1 = Greenland peripheral ice caps; 0 =
        # Ocean.
        mask = mask_data == 0

        masked_data = apply_mask(
            source_data,
            mask,
            source_nodata
        )

        with temporary_path_dir(self.output()) as tmp_dir:
            out_path = os.path.join(tmp_dir, self.filename)
            with rasterio.open(out_path, 'w', **source_profile) as output_ds:
                output_ds.write(masked_data, 1)


class MaskedRacmoRaster(LayerPipeline):

    def requires(self):
        source = self.cfg['source']
        source_dirname = datasource_dirname(
            dataset_id=self.cfg['dataset']['id'],
            source_id=self.cfg['source']['id']
        )
        source_dir = os.path.join(TaskType.FETCH.value, source_dirname)
        mask_filename = 'Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc'
        mask_fp = f'netcdf:{source_dir}/{mask_filename}:Promicemask'

        fetch_data = FetchLocalDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=unzip,
            layer_id=self.layer_id,
        )  # ->
        gdaledit = GdalEdit(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id
        )  # ->
        applied_mask = ApplyPromiceMask(
            requires_task=gdaledit,
            layer_id=self.layer_id,
            mask_fp=mask_fp
        )  # ->
        warp_raster = WarpRaster(
            requires_task=applied_mask,
            layer_id=self.layer_id
        )  # ->
        return BuildRasterOverviews(
            requires_task=warp_raster,
            layer_id=self.layer_id
        )
