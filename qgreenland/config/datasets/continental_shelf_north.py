from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


north_points = Dataset(
    id='north_points',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_points.zip',
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

north_lines = Dataset(
    id='north_lines',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_lines.zip',
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

north_points = Dataset(
    id='north_polygons',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_polygons.zip',
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