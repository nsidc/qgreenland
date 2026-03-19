from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

layer = Layer(
    id="municipalities_and_population",
    title="Greenland municipalities and population (temporal)",
    description=(
        """Polygons representing municipalities of Greenland and associated
        population numbers from 1976-2024.

        Note: to use this layer, enable the temporal controller and set a
        specific year to see that year's population statistics. Without the
        temporal controller enabled, the earliest population statistics will be
        shown (for 1976).
        """
    ),
    tags=[],
    in_package=True,
    style="municipalities_pop_timeseries",
    inputs=[
        VectorLayerReferenceInput(
            layer_id="nunagis_municipalities",
            sql=(
                """SELECT
                    municipalities.geom,
                    municipalities.municipality,
                    pop.start_date,
                    pop.end_date,
                    pop.\"Population January 1st\" as population
                    FROM municipalities
                    RIGHT JOIN pop ON pop.municipality
                    = municipalities.municipality"""
            ),
        )
    ],
    steps=[],
)
