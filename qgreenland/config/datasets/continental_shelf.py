from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


continental_shelf = Dataset(
    id='continental_shelf',
    assets=[
        HttpAsset(
            id='north_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_points.zip',
            ],
        ),
        HttpAsset(
            id='north_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_lines.zip',
            ],
        ),
        HttpAsset(
            id='north_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_polygons.zip',
            ],
        ),
        HttpAsset(
            id='northeast_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip',
            ],
        ),
        HttpAsset(
            id='northeast_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip',
            ],
        ),
        HttpAsset(
            id='northeast_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip',
            ],
        ),
        HttpAsset(
            id='south_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip',
            ],
        ),
        HttpAsset(
            id='south_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip',
            ],
        ),
        HttpAsset(
            id='south_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip',
            ],
        ),
    ],
    metadata={
        'title': "Denmark - in respect of the Continental Shelf of Greenland",
        'abstract': (
            """TODO: ."""
        ),
        'citation': {
            'text': (
                """TODO: ."""
            ),
            'url': 'http://example.com',
        },
    },
)
