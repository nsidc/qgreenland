from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


seismograph_stations = ConfigDataset(
    id='seismograph_stations',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'http://www.isc.ac.uk/registries/download/stations.kmz',
            ],
        ),
    ],
    metadata={
        'title': 'International Registry of Seismograph Stations (IR)',
        'abstract': (
            """The International Seismograph Station Registry (IR) has been
            jointly maintained by the International Seismological Centre (ISC)
            and the World Data Center for Seismology (NEIC/USGS) since the
            1960s. At present there are over 26000 stations (including those
            already closed) with globally unique codes registered in the IR."""
        ),
        'citation': {
            'text': (
                """International Seismological Centre (2020), International
                Seismograph Station Registry (IR),
                https://doi.org/10.31905/EL3FQQ40"""
            ),
            'url': 'http://www.isc.ac.uk/registries/',
        },
    },
)
