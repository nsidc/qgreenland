from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.layers.naturemap import layers_cfg
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

layers = [
    Layer(
        id=layer_id,
        title=layer_cfg["title"],
        description=layer_cfg["description"],
        tags=[],
        in_package=True,
        style=layer_cfg["style"],
        inputs=[
            LayerInput(
                dataset=dataset,
                asset=dataset.assets[layer_id],
            )
        ],
        steps=[
            *ogr2ogr(
                input_file="{input_dir}/*.gpkg",
                output_file="{output_dir}/final.gpkg",
                ogr2ogr_args=layer_cfg["ogr2ogr_args"],
            ),
        ],
    )
    for layer_id, layer_cfg in layers_cfg.items()
]
