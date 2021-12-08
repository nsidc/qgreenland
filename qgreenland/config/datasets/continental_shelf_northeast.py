from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


northeast_points = Dataset(
    id='northeast_points',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_points.zip',
            ],
        ),
    ],
    metadata={
        'title': "Denmark - in respect of the Continental Shelf of Greenland",
        'abstract': (
            """ """
        ),
        'citation': {
            'text': (
                """ """
            ),
            'url': ' ',
        },
    },
)

northeast_lines = Dataset(
    id='northeast_lines',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_lines.zip',
            ],
        ),
    ],
    metadata={
        'title': "Denmark - in respect of the Continental Shelf of Greenland",
        'abstract': (
            """ """
        ),
        'citation': {
            'text': (
                """ """
            ),
            'url': ' ',
        },
    },
)

northeast_polygons = Dataset(
    id='northeast_polygons',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip',
            ],
        ),
    ],
    metadata={
        'title': "Denmark - in respect of the Continental Shelf of Greenland",
        'abstract': (
            """ """
        ),
        'citation': {
            'text': (
                """ """
            ),
            'url': ' ',
        },
    },
)