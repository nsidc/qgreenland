# TODO: Cleanup all comments that aren't specific to your dataset.
# TODO: Fill in and uncomment below:
# from qgreenland.models.config.asset import {your_asset_class}
from qgreenland.models.config.dataset import ConfigDataset


# The name of the `dataset` variable doesn't matter here.
dataset = ConfigDataset(
    # TODO: Fill in `your_dataset_id`. Be descriptive:
    id='your_dataset_id',
    assets=[
        # TODO: Your assets here. See `qgreenland/models/config/assets.py` for
        # available asset types and # their parameters. e.g.:
        # 
        #     ConfigDatasetHttpAsset(
        #         id='only',
        #         urls=['http://example.com/example_asset.tif'],
        #     ),
    ],
    # TODO: Fill in _all_ metadata fields below:
    metadata={
        'title': 'Your dataset title',
        'abstract': (
          """Your dataset abstract."""
        ),
        'citation': {
            'text': (
                """Your dataset citation"""
            ),
            'url': 'https://your.dataset/citation/url',
        },
    },
)
