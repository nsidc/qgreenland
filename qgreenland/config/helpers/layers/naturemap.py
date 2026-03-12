from typing import Any

from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

BIRDS_LAYERS_CFG = {
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
        "style": "barnacle_goose_colonies",
    },
    "goose_moulting_and_breeding_areas": {
        "title": "Goose moulting and breeding areas",
        "description": ("""Polygons representing goose moulting and breeding areas."""),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
}

PROTECTED_ZONES_LAYERS_CFG = {
    "salt_or_saline_lake_100m_zone": {
        "title": "Salt or saline lake 100m zones",
        "description": ("""Polygons representing salt or saline lake 100m zones."""),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    }
}


def _make_layer(layer_id, layer_cfg: dict[str, Any]):
    return Layer(
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


def make_birds_layers():
    layers = [
        _make_layer(layer_id, layer_cfg)
        for layer_id, layer_cfg in BIRDS_LAYERS_CFG.items()
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

    layers.append(seabird_regulated_areas_layer)

    return layers


def make_protected_zones_layers():
    layers = [
        _make_layer(layer_id, layer_cfg)
        for layer_id, layer_cfg in PROTECTED_ZONES_LAYERS_CFG.items()
    ]

    return layers
