from qgreenland.config.datasets.caff import caff_murre_colonies as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


murre_layers = {
    'common_murre': {
        'name': 'Common Murre',
    },
    'thickbilled_murre': {
        'name': 'Thickbilled Murre',
    },
}

layers = [
    ConfigLayer(
        id=f'caff_{key}_colonies',
        title=f'{params["name"]} colonies 2010',
        description=(
            f"""Point locations of {params['name']} colonies as surveyed in
            2010."""
        ),
        tags=[],
        style=f'{key}_colonies',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            *zipped_vector(
                input_file='{input_dir}/Murres_distribution.zip',
                output_file='{output_dir}/final.gpkg',
                shapefile_name=(
                    f'Distribution_{params["name"].replace(" ", "_")}_Colonies.shp'
                ),
            )
        ],
    )
    for key, params in murre_layers.items()
]
