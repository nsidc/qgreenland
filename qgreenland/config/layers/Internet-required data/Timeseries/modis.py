from qgreenland.config.datasets.online import gibs
from qgreenland.models.config.layer import Layer, LayerInput

timeseries_usage_description = """This is a Temporal Layer and can be used with QGIS' Temporal Controller panel. See this webpage for more information: https://docs.qgis.org/3.28/en/docs/user_manual/map_views/map_view.html#maptimecontrol ."""

modis_true_color_layers = [
    Layer(
        id=f"modis_{sat_name}_true_color",
        title=f"MODIS {sat_name.capitalize()} true color",
        description=(
            f"""MODIS {sat_name.capitalize()} corrected reflectance true color.

{timeseries_usage_description}"""
        ),
        tags=["online"],
        input=LayerInput(
            dataset=gibs,
            asset=gibs.assets[f"modis_{sat_name}_true_color"],
        ),
    )
    for sat_name in ("terra", "aqua")
]
