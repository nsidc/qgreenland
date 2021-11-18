from qgreenland.models.config.asset import CommandAsset
from qgreenland.models.config.dataset import Dataset

background = Dataset(
    id='background',
    assets=[
        CommandAsset(
            id='high_res',
            args=[
                'wget',
                'https://naciscdn.org/naturalearth/10m/raster/NE2_HR_LC_SR_W.zip',
                '-O', '{output_dir}/NE2_HR_LC_SR_W.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Natural Earth II with Shaded Relief and Water (1:10m)',
        'abstract': 'Natural Earth II (Public Domain).',
        'citation': {
            'text': 'Made with Natural Earth',
            'url': (
                'https://github.com/nvkelso/natural-earth-vector'
                '/blob/master/LICENSE.md'
            ),
        },
    },
)
