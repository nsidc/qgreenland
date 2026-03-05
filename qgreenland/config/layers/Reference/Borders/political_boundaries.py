import qgreenland.config.datasets.political_boundaries as political_boundaries
import qgreenland.config.datasets.statbank as statbank
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

nunagis_municipalities_population = Layer(
    id="nunagis_municipalities_population",
    title="Greenland municipalities and population",
    description=(
        """Polygons representing municipalities of Greenland and associated
        population numbers from 1977-2025."""
    ),
    tags=[],
    style="nunagis_municipalities_population",
    inputs=[
        # This input provides a multipolygon of municipalities and population numbers for 2019
        LayerInput(
            dataset=political_boundaries.nunagis_pop2019_municipalities,
            asset=political_boundaries.nunagis_pop2019_municipalities.assets["only"],
        ),
        # This input provides updated population statistics for 1977-2025 (each
        # stat valid for Jan 1 of the associated year).
        LayerInput(
            dataset=statbank.statbank,
            asset=statbank.statbank.assets["municipalities_population"],
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
                "pop",
            ],
        ),
        CommandStep(
            id="join_data",
            args=[
                "ogr2ogr",
                *STANDARD_OGR2OGR_ARGS,
                "{output_dir}/joined.gpkg",
                "{input_dir}/merged.gpkg",
                "-dialect",
                "sqlite",
                "-sql",
                """\"SELECT
                    municipalities.geom,
                    municipalities.pop_municipality_2019_municip as municipality,
                    pop.\\"Population January 1st\\",
                    DATE(pop.time || '-01-01') as valid_date_str
                    FROM municipalities
                    RIGHT JOIN pop ON pop.municipality
                    LIKE '%' || municipalities.pop_municipality_2019_municip || '%'\"""",
                "-nln",
                "municipalities_and_pop",
            ],
        ),
        # This step creates a new `valid_date` column with the `Date` field
        # type. This has to be done separately because sqlite will cast `DATE()`
        # (selected above) to text type.
        # TODO: this should be a one-liner with `gdal vector set-field-type`,
        # but that requires gdal >=3.12, and we are currently stuck at gdal 3.10
        # because of conflicts with other dependencies (I think pydantic needs
        # to be updated to v2!). It is possible to update gdal to 3.12 in the
        # command environment, which I think would be OK but would lead to a
        # disconnect between the gdal in the main env and the command env. From
        # what I can tell, gdal is only used for generating statistics in the
        # `main` env, which could be accomplished via a subprocess...
        CommandStep(
            id="update_date_field",
            args=[
                # Copy the input data to the output location. The subsequent
                # commands will update the data in-place
                "cp {input_dir}/joined.gpkg {output_dir}/final.gpkg",
                "&&",
                # update the municipalities_and_pop table to include a column
                # with `DATE` type.
                "ogr2ogr",
                "-update",
                "{output_dir}/final.gpkg",
                "{output_dir}/final.gpkg",
                "-dialect",
                "sqlite",
                "-sql",
                """\"ALTER TABLE municipalities_and_pop
                    ADD COLUMN valid_date DATE\"""",
                "&&",
                # Set the column w/ values from the str field.
                "ogr2ogr",
                "-update",
                "{output_dir}/final.gpkg",
                "{output_dir}/final.gpkg",
                "-dialect",
                "sqlite",
                "-sql",
                """\"UPDATE municipalities_and_pop
                    SET valid_date = valid_date_str\"""",
                "&&",
                # drop the str field, which is now unnecessary
                "ogr2ogr",
                "-update",
                "{output_dir}/final.gpkg",
                "{output_dir}/final.gpkg",
                "-dialect",
                "sqlite",
                "-sql",
                """\"ALTER TABLE municipalities_and_pop
                     DROP COLUMN valid_date_str\"""",
            ],
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
