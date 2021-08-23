from qgreenland.models.config.dataset import (
    ConfigDataset,
    ConfigDatasetHttpAsset,
)

background = ConfigDataset(
    id='background',
    assets={
        # 'high_res': high_res_asset,
        'high_res': ConfigDatasetHttpAsset(
            id='high_res',
            urls=['https://naciscdn.org/naturalearth/10m/raster/NE2_HR_LC_SR_W.zip'],
        ),
    },
    metadata={
        'title': 'Natural Earth II with Shaded Relief and Water (1:10m)',
        'abstract': 'Natural Earth II (Public Domain)',
        'citation': {
            'text': 'Made with Natural Earth',
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)
