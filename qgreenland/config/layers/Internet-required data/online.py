from qgreenland.config.datasets.online import image_mosaic, sdfi_topo_map
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

topo_map_layer = Layer(
    id="sdfi_topo_map",
    title="Topographic map of Greenland",
    description=(
        """The Greenland vector data is based on commercial satellite images
            with a resolution of 0.5 m. The images are primarily from the summer
            months in the period from 2017 to 2021. Data is produced and quality
            assured according to ISO standards.

            Vector data from East Greenland (blocks 10 and 12-15 in the figure ) are not
            finally approved, and you will therefore be able to see, for example, sharp
            demarcations between different terrain forms. The data will be updated
            continuously, first half of 2023.

            Greenlandic place names:
            The Language Secretariat (Oqaasileriffik) in Nuuk is the responsible authority
            for place names. It is also the Language Secretariat that has been responsible
            for the correct placement of the approx. 33,000 place names.  The
            Self-Government at Landsplan is the responsible authority for place names for
            cities and residences."""
    ),
    tags=["online"],
    input=LayerInput(
        dataset=sdfi_topo_map,
        asset=sdfi_topo_map.assets["only"],
    ),
)
