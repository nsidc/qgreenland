from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


continental_shelf = Dataset(
    id='continental_shelf',
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