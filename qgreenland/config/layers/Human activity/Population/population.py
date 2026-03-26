from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

populated_municipalities_layer = Layer(
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


populated_places_layer = Layer(
    id="places_and_population",
    title="Populated places (temporal)",
    description=(
        """Points representing populated places and associated
        population numbers from 1976-2024.

        Note that population values do not include numbers for
        undisclosed individuals within each district.

        Note: to use this layer, enable the temporal controller and set a
        specific year to see that year's population statistics. Without the
        temporal controller enabled, the earliest population statistics will be
        shown (for 1976).
        """
    ),
    tags=[],
    in_package=True,
    style="populated_places_timeseries",
    inputs=[
        VectorLayerReferenceInput(
            layer_id="populated_places",
            sql=(
                """SELECT
                    places.*,
                    pop.population,
                    pop.start_date,
                    pop.end_date
                    FROM places
                    RIGHT JOIN pop ON pop.place_id =
                    places.id"""
            ),
        )
    ],
    steps=[],
)
