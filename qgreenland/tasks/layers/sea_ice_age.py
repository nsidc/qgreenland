from qgreenland.tasks.common.command import Commands
from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import ExtractNcDataset
from qgreenland.tasks.common.raster import GdalEdit
from qgreenland.util.luigi import LayerPipeline


class SeaIceAge(LayerPipeline):
    """Experimental layer task using `Commands` task.

    Do not copy.

    This is a temporary hack to resolve a non-standard set of `gdalwarp`
    operations to prevent smearing of data along the 45°E line.
    """

    def requires(self):
        source = self.cfg['source']

        commands = [
            [
                'gdalwarp',
                '-t_srs', 'EPSG:3413',
                '-tr', '12500', '12500',
                '{INPUT}', '{OUTDIR}/reprojected.tif'
            ],
            [
                'gdalwarp',
                '-cutline', self.cfg['boundary']['fp'],
                '-crop_to_cutline',
                '{OUTDIR}/reprojected.tif', '{OUTPUT}'
            ],
        ]

        fetch_data = FetchDataFiles(
            source_cfg=source,
            dataset_cfg=self.cfg['dataset']
        )  # ->
        extract_nc_dataset = ExtractNcDataset(
            requires_task=fetch_data,
            layer_id=self.layer_id,
        )  # ->
        gdal_edited = GdalEdit(
            requires_task=extract_nc_dataset,
            layer_id=self.layer_id,
        )  # ->
        return Commands(
            requires_task=gdal_edited,
            commands=commands,
            layer_id=self.layer_id
        )
