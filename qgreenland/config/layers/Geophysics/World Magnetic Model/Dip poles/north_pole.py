from qgreenland.config.constants import PROJECT_CRS
from qgreenland.config.datasets import wmm
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


geomagnetic_north_pole = ConfigLayer(
    id='wmm_north_poles',
    title='Geomagnetic North dip pole 2020-2025',
    description="""
The locations of northern hemisphere dip poles (2020-2025) from the World
Magnetic Model (WMM) 2020 model.

The geomagnetic dip poles are positions on the Earth's surface where the
geomagnetic field is perpendicular to the ellipsoid, that is, vertical. The
north and south dip poles do not have to be (and are not now) antipodal.

These model dip poles are computed from all the Gauss coefficients using an
iterative method. In 2020.0 the north dip pole computed from WMM2020 is
located at longitude 164.04°E and geodetic latitude 86.50°N and the south
dip pole at longitude 135.88°E and geodetic latitude 64.07°S.
""",
    in_package=True,
    show=False,
    input=ConfigLayerInput(
        dataset=wmm.wmm,
        asset=wmm.wmm.assets['geomagnetic_north_pole'],
    ),
    style='geomagnetic_north_pole',
    steps=[
        # Add a header to the downloaded txt file so that it can be processed as
        # 'csv' by `ogr2ogr`
        ConfigLayerCommandStep(
            type='command',
            args=[
                'sed',
                '"1i longitude latitude year"',
                '{input_dir}/WMM2020_NP.xy',
                '>', '{output_dir}/WMM2020_NP_with_header.xy',
            ],
        ),
        ConfigLayerCommandStep(
            type='command',
            args=[
                'ogr2ogr',
                '-oo', 'X_POSSIBLE_NAMES=longitude',
                '-oo', 'Y_POSSIBLE_NAMES=latitude',
                '-s_srs', 'EPSG:4326',
                '-t_srs', PROJECT_CRS,
                '{output_dir}/geomagnetic_north_pole.gpkg',
                'CSV:{input_dir}/WMM2020_NP_with_header.xy',
            ],
        ),
    ],
)
