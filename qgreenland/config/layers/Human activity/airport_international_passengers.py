from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

populated_municipalities_layer = Layer(
    id="airport_international_passengers",
    title="Airport international passengers (temporal)",
    description=(
        """Points representing airports in Greenland and associated
        monthly international passenger numbers from 2008-2026.

        Note that points are representative of the location of the
        city/settlement in which the airport resides. Points do not directly
        identify the location of the airport itself.

        Note: to use this layer, enable the temporal controller and set a
        specific year/month to see that year/month's international passenger
        statistics. Without the temporal controller enabled, the earliest
        international passenger statistics will be shown (for 2008).
        """
    ),
    tags=[],
    in_package=True,
    style="international_passengers_timeseries",
    inputs=[
        VectorLayerReferenceInput(
            layer_id="populated_places",
            sql=(
                """SELECT
                    places.geom,
                    international_passengers.airport,
                    international_passengers.passengers,
                    international_passengers.start_date,
                    international_passengers.end_date
                    FROM places
                    RIGHT JOIN international_passengers
                    ON international_passengers.place_id = places.id"""
            ),
        )
    ],
    steps=[],
)
