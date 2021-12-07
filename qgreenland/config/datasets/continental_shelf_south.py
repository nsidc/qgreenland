from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


south_points = Dataset(
    id='south_points',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip',
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

south_lines = Dataset(
    id='south_lines',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_lines.zip',
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

south_polygons = Dataset(
    id='south_polygons',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_polygons.zip',
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
