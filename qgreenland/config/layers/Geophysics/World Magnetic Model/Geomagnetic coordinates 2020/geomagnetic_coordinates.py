from qgreenland.config.constants import PROJECT_CRS
from qgreenland.config.datasets import wmm
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


_layers = [
    {
        'id': 'wmm_latitudes',
        'title': 'Geomagnetic latitudes',
        'partial_filename': 'GeomagLatitude_2020',
    },
    {
        'id': 'wmm_longitudes',
        'title': 'Geomagnetic longitudes',
        'partial_filename': 'GeomagLongitude_2020',
    },
]


def _make_layer(
    *,
    id: str,
    title: str,
    partial_filename: str,
) -> ConfigLayer:
    return ConfigLayer(
        id=id,
        title=title,
        description="""
The WMM representation of the field includes a magnetic dipole at the center
of the Earth. This dipole defines an axis that intersects the Earth's
surface at two antipodal points. These points are called geomagnetic
poles. The geomagnetic poles, otherwise known as the dipole poles, can be
computed from the first three Gauss coefficients of the WMM. Based on the
WMM2020 coefficients for 2020.0 the geomagnetic north pole is at 72.68°W
longitude and 80.59°N geocentric latitude (80.65°N geodetic latitude), and
the geomagnetic south pole is at 107.32°E longitude and 80.59°S geocentric
latitude (80.65°S geodetic latitude). The axis of the dipole is currently
inclined at 9.41° to the Earth's rotation axis. The same dipole is the basis
for the simple geomagnetic coordinate system of geomagnetic latitude and
longitude
""",
        in_package=True,
        show=False,
        style='latlon',
        input=ConfigLayerInput(
            dataset=wmm.wmm,
            asset=wmm.wmm.assets['geomagnetic_coordinates'],
        ),
        steps=[
            ConfigLayerCommandStep(
                type='command',
                args=[
                    'unzip',
                    '-j',
                    '-d', '{output_dir}',
                    '{input_dir}/WMM2020_geomagnetic_coordinate_shapefiles.zip',
                    f'"*geographic_projection/*{partial_filename}*"',
                ],
            ),
            ConfigLayerCommandStep(
                type='command',
                args=[
                    'OGR_ENABLE_PARTIAL_REPROJECTION=TRUE',
                    'ogr2ogr',
                    '-t_srs', PROJECT_CRS,
                    '-dialect', 'sqlite',
                    '-sql', (
                        '"Select Geometry, Contour, SIGN, \\"INDEX\\", '
                        "CAST(Contour AS TEXT) || ' °' as label "
                        f'FROM {partial_filename}"'
                    ),
                    '{output_dir}/' + f'{partial_filename}.gpkg',
                    '{input_dir}/' + f'{partial_filename}.shp',
                ],
            ),
        ],
    )


geomagnetic_coordinates_layers = [
    _make_layer(**i) for i in _layers
]
