from qgreenland.config.constants import PROJECT_CRS
from qgreenland.config.datasets import wmm
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def make_boz_layer(*, year: int) -> ConfigLayer:
    return ConfigLayer(
        id=f'wmm_boz_{year}',
        title='Blackout zones',
        description="""
Based on the WMM military specification, we define “Blackout Zones” (BoZ)
around the north and south magnetic poles where compass accuracy is highly
degraded. The BoZ are defined as regions around the north and south magnetic
poles where the horizontal intensity of Earth’s magnetic field (H) is less
than 2000 nT. In BoZs, WMM declination values are not accurate and compasses
are unreliable.

We additionally define a “Caution Zone” (2000 nT <= H < 6000 nT) around the
BoZ, where caution must be exercised while using a compass. Compass accuracy
may be degraded in this region.
""",
        in_package=True,
        show=False,
        style='blackout_zones',
        input=ConfigLayerInput(
            dataset=wmm.wmm,
            asset=wmm.wmm.assets['blackout_zones'],
        ),
        steps=[
            ConfigLayerCommandStep(
                type='command',
                args=[
                    'unzip',
                    '-j',
                    '-d', '{output_dir}',
                    '{input_dir}/WMM2020-2025_BoZ_Shapefile.zip',
                    f'"*BOZ_arctic_all/BOZ_{year}*"',
                ],
            ),
            ConfigLayerCommandStep(
                type='command',
                args=[
                    'ogr2ogr',
                    '-lco', 'ENCODING=UTF-8',
                    '-t_srs', PROJECT_CRS,
                    '-clipdst', '{assets_dir}/latitude_shape_40_degrees.geojson',
                    '{output_dir}/' + f'BOZ_{year}.gpkg',
                    '{input_dir}/' + f'BOZ_{year}.shp',
                ],
            ),
        ],
    )
