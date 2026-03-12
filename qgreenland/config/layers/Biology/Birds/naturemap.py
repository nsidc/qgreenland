from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.layers.naturemap import layers_cfg
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

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
                ogr2ogr_args=layer_cfg["ogr2ogr_args"],  # type: ignore[arg-type]
            ),
        ],
    )
    for layer_id, layer_cfg in layers_cfg.items()
]

seabird_regulated_areas_layer = Layer(
    id="seabird_regulated_areas_layer",
    title="Seabird colony regulated areas",
    description=(
        """Polygons represented regulated areas for seabird colonies.

           See the Attribute Table for information on specific aviation and
           sailing regulations for each area."""
    ),
    tags=[],
    in_package=True,
    style="seabird_colony_regulated_areas",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets[asset_id],
        )
        for asset_id in (
            "seabird_colony_non_disturbance_zone_200m",
            "seabird_colony_non_disturbance_zone_1000m",
            "seabird_colony_no_drone_zone_100m",
            "seabird_colony_no_fly_zone_500m",
            "seabird_colony_no_fly_zone_3000m",
        )
    ],
    steps=[
        CommandStep(
            id="ogrmerge",
            args=[
                "ogrmerge",
                "-o",
                "{output_dir}/merged.gpkg",
                "{input_dir}/*.gpkg",
                "-single",
            ],
        ),
        *ogr2ogr(
            input_file="{input_dir}/merged.gpkg",
            output_file="{output_dir}/final.gpkg",
            ogr2ogr_args=(
                "-sql",
                (
                    """\"SELECT *,
                    COALESCE(
                        'Aviation: ' || regulationAviation,
                        'Sailing: ' || regulationSailing,
                        'UAV: ' || regulationUAV,
                        'Other: ' || regulationOther
                    )
                    AS regulation
                    FROM merged\""""
                ),
                "-nln",
                "seabird_regulated_areas",
            ),
        ),
    ],
)
