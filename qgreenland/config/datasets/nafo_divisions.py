from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


nafo_divisions = ConfigDataset(
    id='nafo_divisions',
    assets=[
        ConfigDatasetHttpAsset(
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
