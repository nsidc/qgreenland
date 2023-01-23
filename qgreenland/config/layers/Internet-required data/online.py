from qgreenland.config.datasets.online import image_mosaic
from qgreenland.models.config.layer import Layer, LayerInput

image_mosaic_layers = [
    Layer(
        id=f"image_mosaic_{year}",
        title=f"Greenland image mosaic {year} ({resolution}m)",
        description=f"Sentinel-2 multispectral satellite imagery from {year}.",
        tags=["online"],
        style="transparent_rgb",
        input=LayerInput(
            dataset=image_mosaic,
            asset=image_mosaic.assets[year],
        ),
    )
    for year, resolution in (("2015", "15"), ("2019", "10"))
]
