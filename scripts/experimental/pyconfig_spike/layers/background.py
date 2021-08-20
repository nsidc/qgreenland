from qgreenland.models.config.layer import ConfigLayer

from scripts.experimental.pyconfig_spike.datasets.natural_earth import background as background_dataset

background = ConfigLayer(
    id='background',
    title='Background (500m)',
    description='Stylized shaded-relief map for providing a general sense of geography.',
    hierarchy=['Basemaps'],
    in_package=True,
    show=True,
    input={
        'dataset': background_dataset,
        'asset': background_dataset.assets['high_res'],
    },
    steps=[],
)

print(background.json(indent=4))
