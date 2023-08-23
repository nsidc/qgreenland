from qgreenland.config.datasets.online import geus_geological_map
from qgreenland.models.config.layer import Layer, LayerInput

geus_geological_map_layer = Layer(
    id="geus_geological_map",
    title="Geological Map (1:500 000)",
    description=(
        """Map showing geological features of Greenland.

        Please download the legend for information on interpretation
        of this layer:
        https://maps.greenmin.gl/geusmapmore/greenlandportal/G500_2023_LEGEND.pdf .
        """
    ),
    tags=["online"],
    input=LayerInput(
        dataset=geus_geological_map,
        asset=geus_geological_map.assets["only"],
    ),
)
