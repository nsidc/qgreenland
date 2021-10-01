from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


nga_arctic_sea_routes = ConfigDataset(
    id='nga_arctic_sea_routes',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                (
                    'https://opendata.arcgis.com/datasets/67760a7f85614902ac19fa6ff643b9fa_0.zip?'
                    'outSR=%7B%22latestWkid%22%3A102018%2C%22wkid%22%3A102018%7D'
                ),
            ],
        ),
    ],
    metadata={
        'title': 'Arctic Sea Routes',
        'abstract': (
            """Arctic lines of general transportation. In the case of the
            Northern Sea Route, the route is based on the actual route used by
            Russian icebreakers and cargo ships. The Northwest Passage is based
            on the channels that would be able to support large cargo ships. The
            transpolar route is a hypothetical route that could be used either
            as a result of ice-free summers or the extensive use of icebreakers
            and ice-hardened ships."""
        ),
        'citation': {
            'text': (
                """National Geospatial-Intelligence Agency (NGA)"""
            ),
            'url': 'https://arctic-nga.opendata.arcgis.com/datasets/67760a7f85614902ac19fa6ff643b9fa_0',
        },
    },
)
