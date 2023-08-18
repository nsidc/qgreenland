from qgreenland.config.datasets.grimp import grimp_annual_ice_velocity as dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.models.config.layer import Layer, LayerInput

grimp_vv_veloity_layers = [
    Layer(
        id=layer_id,
        # TODO: better title.
        title=layer_id,
        description="TODO.",
        # TODO:
        style=None,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[layer_id],
        ),
        steps=[
            *compress_and_add_overviews(
                input_file="{input_dir}/*_vv_*.tif",
                output_file="{output_dir}/vv.tif",
                dtype_is_float=True,
            ),
        ],
    )
    for layer_id in [f"vv_{year}" for year in range(2015, 2021 + 1)]
]
