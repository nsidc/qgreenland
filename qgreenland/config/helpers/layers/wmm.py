from typing import Literal

from qgreenland.config.datasets import wmm
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.config.project import project
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
        tags=['wmm'],
        in_package=True,
        show=False,
        style='blackout_zones',
        input=ConfigLayerInput(
            dataset=wmm.wmm,
            asset=wmm.wmm.assets['blackout_zones'],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'unzip',
                    '-j',
                    '-d', '{output_dir}',
                    '{input_dir}/WMM2020-2025_BoZ_Shapefile.zip',
                    f'"*BOZ_arctic_all/BOZ_{year}*"',
                ],
            ),
            ConfigLayerCommandStep(
                args=[
                    'ogr2ogr',
                    '-lco', 'ENCODING=UTF-8',
                    '-t_srs', project.crs,
                    '-clipdst', project.boundaries['background'].filepath,
                    '{output_dir}/' + f'BOZ_{year}.gpkg',
                    '{input_dir}/' + f'BOZ_{year}.shp',
                ],
            ),
        ],
    )


WmmVariable = Literal[
    'd',
    'd_sv',
    'f',
    'f_sv',
    'h',
    'h_sv',
    'i',
    'i_sv',
    'x',
    'x_sv',
    'y',
    'y_sv',
    'z',
    'z_sv',
]
WmmVariableParameter = Literal['title', 'description', 'contour_units']
WmmVariableParameterDict = dict[WmmVariableParameter, str]
WmmVariableDict = dict[WmmVariable, WmmVariableParameterDict]
# NOTE: the order of this dictionary determines the layer order produced by
# `wmm_layer_order`
_wmm_variable_config: WmmVariableDict = {
    'd': {
        'title': 'Main field declination (D)',
        'description': """
Contours representing magnetic declination (D) in degrees. D is the angle
between magnetic north and true north. D is considered positive when the
angle measured is east of true north and negative when west.
""",
        'contour_units': '°',
    },

    'd_sv': {
        'title': 'Annual change declination (D_SV)',
        'description': """
Contours representing annual change (secular variation) in the declination
(D) of the main magnetic field in arcminutes per year.
""",
        'contour_units': "''/y",
    },

    'f': {
        'title': 'Main field total intensity (F)',
        'description': """
Contours representing the intensity of the total field (F) in nanoTesla
(nT). F is described by the horizontal component (H), vertical component
(Z), and the north (X) and east (Y) components of the horizontal
intensity. The Earth's magnetic field intensity is roughly between 25,000 -
65,000 nT (.25 - .65 gauss).
""",
        'contour_units': 'nT',
    },

    'f_sv': {
        'title': 'Annual change total intensity (F_SV)',
        'description': """
Contours representing annual change (secular variation) in the total
intensity (F) of the main magnetic field in nanoTesla per year.
""",
        'contour_units': 'nT/y',
    },

    'h': {
        'title': 'Main field horizontal intensity (H)',
        'description': """
Contours representing Horizontal Intensity (H) of the geomagnetic main field
in nanoTesla (nT).
""",
        'contour_units': 'nT',
    },

    'h_sv': {
        'title': 'Annual change horizontal intensity (H_SV)',
        'description': """
Contours representing annual change (secular variation) in the horizontal
intensity (H) of the main magnetic field in nanoTesla per year.
""",
        'contour_units': 'nT/y',
    },

    'i': {
        'title': 'Main field inclination (I)',
        'description': """
Contours representing magnetic inclination (I) in degrees. I is the angle
between the horizontal plane and the total field vector, measured positive into
Earth.
""",
        'contour_units': '°',
    },

    'i_sv': {
        'title': 'Annual change inclination (I_SV)',
        'description': """
Contours representing annual change (secular variation) in the magnetic
inclination (I) of the main magnetic field in arcminutes per year.
""",
        'contour_units': "''/y",
    },

    'x': {
        'title': 'Main field North component (X)',
        'description': """
Contours representing the main field North component (X) of the horizontal
intensity in nanoTesla (nT).
""",
        'contour_units': 'nT',
    },

    'x_sv': {
        'title': 'Annual change North component (X_SV)',
        'description': """
Contours representing annual change (secular variation) in the North
component (X) of the horizontal intensity of the main magnetic field in
nanoTesla per year.
""",
        'contour_units': 'nT/y',
    },

    'y': {
        'title': 'Main field East component (Y)',
        'description': """
Contours representing the main field East component (Y) of the horizontal
intensity in nanoTesla (nT).
""",
        'contour_units': 'nT',
    },

    'y_sv': {
        'title': 'Annual change East component (Y_SV)',
        'description': """
Contours representing annual change (secular variation) in the East component
(Y) of the horizontal intensity of the main magnetic field in nanoTesla per
year.
""",
        'contour_units': 'nT/y',
    },

    'z': {
        'title': 'Main field down component (Z)',
        'description': """
Contours representing the main field down component (Z) in nanoTesla (nT).
""",
        'contour_units': 'nT',
    },

    'z_sv': {
        'title': 'Annual change down component (Z_SV)',
        'description': """
Contours representing annual change (secular variation) in the down component
(Z) of the main magnetic field in nanoTesla per year.
""",
        'contour_units': 'nT/y',
    },
}


def unzip_and_reproject_wmm_vector(
    *,
    partial_filename: str,
    contour_units: str,
    unzip_contents_mask: str,
    zip_filename: str,
) -> list[ConfigLayerCommandStep]:
    unzip = ConfigLayerCommandStep(
        args=[
            'unzip',
            '-j',
            '-d', '{output_dir}',
            '{input_dir}/' + zip_filename,
            unzip_contents_mask,
        ],
    )

    reproject_with_sql = ConfigLayerCommandStep(
        args=[
            'OGR_ENABLE_PARTIAL_REPROJECTION=TRUE',
            'ogr2ogr',
            '-lco', 'ENCODING=UTF-8',
            '-t_srs', project.crs,
            '-clipdst', project.boundaries['background'].filepath,
            '-dialect', 'sqlite',
            '-sql', (
                r'"Select Geometry, Contour, SIGN, \"INDEX\", '
                fr'CAST(Contour AS TEXT) || \" {contour_units}\" as label '
                f'FROM {partial_filename}"'
            ),
            '{output_dir}/' + f'{partial_filename}.gpkg',
            '{input_dir}/' + f'{partial_filename}.shp',
        ],
    )

    return [unzip, reproject_with_sql]


def make_wmm_variable_layer(
    *,
    variable: WmmVariable,
    year: int,
) -> ConfigLayer:
    variable_config = _wmm_variable_config[variable]
    contour_label = variable_config['contour_units']

    return ConfigLayer(
        id=f'wmm_{variable}_{year}',
        title=variable_config['title'],
        description=variable_config['description'],
        in_package=True,
        style='wmm_contours',
        input=ConfigLayerInput(
            dataset=wmm.wmm,
            asset=wmm.wmm.assets[str(year)],
        ),
        steps=unzip_and_reproject_wmm_vector(
            zip_filename=f'WMM_{year}_all_shape_geographic.zip',
            unzip_contents_mask=f'*{variable.upper()}_{year}*',
            partial_filename=f'{variable.upper()}_{year}',
            contour_units=contour_label,
        ),
    )


def make_wmm_variable_layers_for_year(*, year: int) -> list[ConfigLayer]:
    layers = []
    variable_names = _wmm_variable_config.keys()

    blackout_zones_layer = make_boz_layer(year=year)
    layers.append(blackout_zones_layer)

    for variable_name in variable_names:
        layers.append(
            make_wmm_variable_layer(variable=variable_name, year=year),
        )

    return layers


def wmm_layer_order(*, year: int, layer_filename: str) -> list[str]:
    layer_order = []
    layer_order.append(f'{layer_filename}:wmm_boz_{year}')
    for variable_name in _wmm_variable_config.keys():
        layer_order.append(f'{layer_filename}:wmm_{variable_name}_{year}')

    return layer_order
