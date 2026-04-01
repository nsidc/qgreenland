from qgreenland.models.config.layer import Layer, VectorLayerReferenceInput

layer = Layer(
    id="total_fish_shellfish_landings",
    title="Total fish and shellfish landings in tonnes (temporal)",
    description=(
        """Points representing districts in Greenland and associated numbers of
        fish and shellfish landings by month between Jan. 2012- Feb. 2026.

        Note: to use this layer, enable the temporal controller and set a
        specific year/month to see that year/month's statistics. Without the
        temporal controller enabled, the earliest statistics will be shown.
        """
    ),
    tags=[],
    in_package=True,
    style="total_fish_shellfish_landings_timeseries",
    inputs=[
        VectorLayerReferenceInput(
            layer_id="populated_places",
            sql=(
                """SELECT
                    places.geom,
                    total_fish_shellfish_landings.district,
                    total_fish_shellfish_landings.landings_fish_and_shellfish_tonnes,
                    total_fish_shellfish_landings.start_date,
                    total_fish_shellfish_landings.end_date
                    FROM places
                    RIGHT JOIN total_fish_shellfish_landings
                    ON total_fish_shellfish_landings.place_id = places.id"""
            ),
        )
    ],
    steps=[],
)
