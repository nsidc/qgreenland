from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

populated_municipalities_layer = Layer(
    id="cruise_passengers",
    title="Cruise passengers by harbor (temporal)",
    description=(
        """Points representing harbors in Greenland and associated
        monthly curise passenger numbers from 2015-2025

        Note that points are representative of the location of the
        city/settlement in which the harbor resides. Points do not directly
        identify the location of the harbor itself.

        Note: to use this layer, enable the temporal controller and set a
        specific year/month to see that year/month's cruise passenger
        statistics. Without the temporal controller enabled, the earliest
        cruise passenger statistics will be shown (for 2015).
        """
    ),
    tags=[],
    in_package=True,
    style="cruise_passengers_timeseries",
    inputs=[
        VectorLayerReferenceInput(
            layer_id="populated_places",
            sql=(
                """SELECT
                    places.geom,
                    cruise_passengers.port,
                    cruise_passengers.passengers,
                    cruise_passengers.start_date,
                    cruise_passengers.end_date
                    FROM places
                    RIGHT JOIN cruise_passengers
                    ON cruise_passengers.place_id = places.id"""
            ),
        )
    ],
    steps=[],
)
