from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


mineral_and_hydrocarbon_licenses = Dataset(
    id='mineral_and_hydrocarbon_licenses',
    assets=[
        HttpAsset(
            id='mcas_mlsa_public_all',
            urls=[
                'https://gis.govmin.gl/geoserver/MLSA/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=shape-zip&typeNames=MLSA:mcas_mlsa_public_all',
            ],
        ),
        HttpAsset(
            id='mcas_mlsa_public_historic',
            urls=[
                'https://gis.govmin.gl/geoserver/MLSA/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=shape-zip&typeNames=MLSA:mcas_mlsa_public_historic',
            ],
        ),
    ],
    metadata={
        'title': 'Mineral and hydrocarbon licenses',
        'abstract': (
            """Mineral and hydrocarbon license data, including historic public
            licenses and public licenses. License data is sourced from the
            Mineral Resource Authority, Government of Greenland using their
            GeoServer version 2.14.1 (https://gis.govmin.gl/geoserver/web/)."""
        ),
        'citation': {
            'text': 'Government of Greenland/GINR',
            'url': '',
        },
    },
)
