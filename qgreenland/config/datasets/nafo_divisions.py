from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


nafo_divisions = Dataset(
    id='nafo_divisions',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.nafo.int/Portals/0/GIS/Divisions.zip',
            ],
        ),
    ],
    metadata={
        'title': 'NAFO Divisions',
        'abstract': (
            """The Northwest Atlantic Fisheries Organization (NAFO) Secretariat
            is a repository of information and meta-data related to the fishery,
            including catch statistics, scientific literature, fisheries
            management documentation and GIS (geographic information system)
            resources. Users can find additional data at the citation URL."""
        ),
        'citation': {
            'text': (
                """Northwest Atlantic Fisheries Organization Secretariat"""
            ),
            'url': 'https://www.nafo.int/Data',
        },
    },
)
