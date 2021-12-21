from qgreenland.config.datasets.wdmam import (
    wdmam as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


layer = Layer(
    id='wdmam',
    title='World Digital Magnetic Anomaly Map',
    description=(
        """Points representing magnetic anomalies in nanoTesla (nT).

        The altitude is 5 km above the WGS84 ellipsoid, except for the marine
        data and model (indexes 11 and 44) where altitude is the sea level
        (0). Magnetic anomalies ('magnetic_anomaly') are computed with reference
        to geomagnetic field model CM4 for year 1990. During the processing,
        ('index') is removed from the original data grid and replaced by
        ('long_wavelength') to obtain ('magnetic_anomaly'). The original
        magnetic anomaly data grid can therefore be restored by adding ('index')
        and removing ('long_wavelength') from ('magnetic_anomaly')."""
    ),
    tags=[],
    in_package=False,
    style='wdmam',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        CommandStep(
            id='convert_to_csv',
            args=[
                'sed',
                # Trim leading whitespace
                '-e',
                r'"s/^\s\+//g"',
                # Replace all other whitespace with ','
                '-e',
                r'"s/\s\+/,/g"',
                # Add a header
                '-e',
                '1i"longitude,latitude,magnetic_anomaly,index,long_wavelength"',
                '{input_dir}/full_wdmam.xyz',
                '>',
                '{output_dir}/full_wdmam.csv',
            ],
        ),
        *ogr2ogr(
            input_file='{input_dir}/full_wdmam.csv',
            output_file='{output_dir}/wdmam_greenland.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=[
                '-oo', 'X_POSSIBLE_NAMES=longitude',
                '-oo', 'Y_POSSIBLE_NAMES=latitude',
                '-oo', 'AUTODETECT_TYPE=True',
                '-s_srs', 'EPSG:4326',
            ],
        ),
    ],
)
