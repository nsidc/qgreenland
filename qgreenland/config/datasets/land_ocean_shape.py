from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


land_shape = Dataset(
    id='land_shape',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Natural Earth Land (10m)',
        'abstract': (
            """Natural Earth Land (Public Domain)."""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)

ocean_shape = Dataset(
    id='ocean_shape',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_ocean.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Natural Earth Ocean (10m)',
        'abstract': (
            """Natural Earth Ocean (Public Domain)."""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)
