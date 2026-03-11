from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

layers_cfg = {
    "barnacle_goose_colony": {
        "title": "Barnacle goose colonies",
        "description": (
            """Shows the position of breeding colonies for barnacle goose from
               2000. Note that unrecorded important goose areas might exist,
               particularly in remote areas."""
        ),
        # Convert from polygon to point. The layer natively uses polygons to
        # represent points, but these are not easily scalable for visualization
        # purposes.
        "ogr2ogr_args": (
            "-sql",
            '"SELECT ST_CENTROID(SHAPE) as geom, * FROM Barnacle_goose_colony"',
            "-nlt",
            "POINT",
            "-nln",
            "barnacle_goose_colony",
        ),
    },
}


layers = [
    Layer(
        id=layer_id,
        title=layer_cfg["title"],
        description=layer_cfg["description"],
        tags=[],
        in_package=True,
        # TODO
        # style=layer_cfg["style"],
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
