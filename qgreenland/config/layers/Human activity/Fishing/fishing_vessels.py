from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

vessel_types = [
    "Dinghies",
    "Fishing vessels",
    "Dog sledge",
    "Snow mobile",
]

layers = [
    Layer(
        id="fishing_vessels_" + "_".join(vessel_type.split()).lower(),
        title=f"Number of {vessel_type.lower()} used for fishing (temporal)",
        description=(
            f"""Points representing districts in Greenland and associated
            yearly numbers of {vessel_type.lower()} used in fishing from 2019-2024.

            Note: to use this layer, enable the temporal controller and set a
            specific year to see that year's statistics. Without the temporal
            controller enabled, the earliest statistics will be shown.
            """
        ),
        tags=[],
        in_package=True,
        style="fishing_vessels_timeseries",
        inputs=[
            VectorLayerReferenceInput(
                layer_id="populated_places",
                sql=(
                    f"""SELECT
                        places.geom,
                        fishing_vessels.District,
                        fishing_vessels.number_of_vessels,
                        fishing_vessels.start_date,
                        fishing_vessels.end_date
                        FROM places
                        RIGHT JOIN fishing_vessels
                        ON fishing_vessels.place_id = places.id
                        WHERE fishing_vessels.vessel_type = '{vessel_type}'"""
                ),
            )
        ],
        steps=[],
    )
    for vessel_type in vessel_types
]
