import qgreenland.config.datasets.political_boundaries as political_boundaries
import qgreenland.config.datasets.statbank as statbank
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

nunagis_municipalities_population = Layer(
    id="nunagis_municipalities_population",
    title="Greenland municipalities and population",
    description=(
        """Polygons representing municipalities of Greenland and associated
        population numbers for 2019 and 2025."""
    ),
    tags=[],
    style="nunagis_municipalities_population",
    inputs=[
        # This input provides a multipolygon of municipalities and population numbers for 2019
        LayerInput(
            dataset=political_boundaries.nunagis_pop2019_municipalities,
            asset=political_boundaries.nunagis_pop2019_municipalities.assets["only"],
        ),
        # This input provides updated population statistics for 2025 (Jan 1, 2026).
        LayerInput(
            dataset=statbank.statbank,
            asset=statbank.statbank.assets["municipalities_2025_population"],
        ),
    ],
    steps=[
        CommandStep(
            id="merge_datasets",
            args=[
                "ogr2ogr",
                "{output_dir}/merged.gpkg",
                "{input_dir}/fetched.geojson",
                "-nln",
                "municipalities",
                "&&",
                "ogr2ogr",
                "-update",
                "{output_dir}/merged.gpkg",
                "{input_dir}/BEXSTB.csv",
                "-nln",
                "pop2025",
            ],
        ),
        CommandStep(
            id="join_data",
            args=[
                "ogr2ogr",
                "{output_dir}/joined.gpkg",
                "{input_dir}/merged.gpkg",
                "-dialect",
                "sqlite",
                "-sql",
                """\"SELECT
                    municipalities.geom,
                    municipalities.pop_municipality_2019_municip as municipality,
                    municipalities.pop_municipality_2019_populatio as \\"Population 2019\\",
                    pop2025.\\"Population January 1st\\" as \\"Population 2025\\"
                    FROM municipalities
                    JOIN pop2025 ON pop2025.municipality
                    LIKE '%' || municipalities.pop_municipality_2019_municip || '%'\"""",
                "-nln",
                "municipalities_and_pop",
            ],
        ),
        # Standard options
        # TODO: necessary? Could merge standard options with ogr2ogr command
        # above...
        *ogr2ogr(
            input_file="{input_dir}/joined.gpkg",
            output_file="{output_dir}/nunagis_municipalities_population.gpkg",
        ),
    ],
)

ne_states_provinces = Layer(
    id="ne_states_provinces",
    title="Global administrative divisions",
    description=(
        """Polygons representing countries' internal administrative
        boundaries."""
    ),
    tags=[],
    style="administrative_divisions",
    inputs=[
        LayerInput(
            dataset=political_boundaries.ne_states_provinces,
            asset=political_boundaries.ne_states_provinces.assets["only"],
        )
    ],
    steps=[
        *compressed_vector(
            input_file="{input_dir}/ne_10m_admin_1_states_provinces.zip",
            output_file="{output_dir}/ne_states_provinces.gpkg",
        ),
    ],
)

ne_countries = Layer(
    id="ne_countries",
    title="Countries",
    description=("""Polygons representing countries."""),
    tags=[],
    style="countries",
    inputs=[
        LayerInput(
            dataset=political_boundaries.ne_countries,
            asset=political_boundaries.ne_countries.assets["only"],
        )
    ],
    steps=[
        *compressed_vector(
            input_file="{input_dir}/ne_10m_admin_0_countries.zip",
            output_file="{output_dir}/ne_countries.gpkg",
        ),
    ],
)
