from qgreenland.config.datasets.ice_isopachs import ice_iso_map as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ice_iso_map = ConfigLayer(
    id='ice_iso_map',
    title='Ice Isopachs',
    description=(
        """Onshore ice isopachs for the landmass of Greenland."""
    ),
    tags=[],
    # TODO: export stylesheet
    # style='ice_isopachs',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/as_2159.zip',
            decompress_step_kwargs={
                'decompress_contents_mask': 'data/shape/base/Greenland_ice.*',
            },
            output_file='{output_dir}/final.gpkg',
            vector_filename='data/shape/base/Greenland_ice.shp',
        ),
    ],
)
