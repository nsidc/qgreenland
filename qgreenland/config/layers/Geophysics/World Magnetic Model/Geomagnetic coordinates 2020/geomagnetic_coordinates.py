from qgreenland.config.datasets import wmm
from qgreenland.config.helpers.layers.wmm import unzip_and_reproject_wmm_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


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
longitude.
""",
        in_package=True,
        show=False,
        style='latlon',
        input=ConfigLayerInput(
            dataset=wmm.wmm,
            asset=wmm.wmm.assets['geomagnetic_coordinates'],
        ),
        steps=unzip_and_reproject_wmm_vector(
            zip_filename='WMM2020_geomagnetic_coordinate_shapefiles.zip',
            unzip_contents_mask=f'"*geographic_projection/*{partial_filename}*"',
            partial_filename=partial_filename,
            contour_units='°',
        ),
    )


geomagnetic_coordinates_layers = [
    _make_layer(**i) for i in _layers
]
