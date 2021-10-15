from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


ocean_shape = ConfigDataset(
    id='ocean_shape',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_ocean.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Natural Earth Ocean (10m)',
        'abstract': (
            """Natural Earth Ocean (Public Domain)"""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)
