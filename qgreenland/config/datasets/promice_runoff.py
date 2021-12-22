from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


# TODO: How to create a layer using this data? The NETCDF files are composed of
# daily runoff amounts predicted by a climate model for each basin in the
# streams_outlets_basins dataset.
promice_runoff = Dataset(
    id='promice_runoff',
    assets=[
        HttpAsset(
            id=f'land_mar_{year}',
            urls=[
                f'https://promice.org/PromiceDataPortal/api/download/0f9dc69b-2e3c-43a2-a928-36fbb88d7433/version_01/runoff/coast/runoff_land_MAR_{year}.nc',
            ],
        ) for year in range(2010, 2017 + 1)
    ],
    metadata={
        'title': 'Map of GC-Net and PROMICE locations',
        'abstract': (
            """High resolution map of Greenland hydrologic outlets, basins, and
            streams, and a 1979 through 2017 time series of Greenland liquid
            water runoff for each outlet."""
        ),
        'citation': {
            'text': (
                """Mankoff et al. - submitted to ESSD."""
            ),
            'url': 'https://doi.org/10.22008/promice/data/freshwater_runoff/v01',
        },
    },
)
