from qgreenland.config.datasets.online import (
    geus_geological_map,
    gibs,
    image_mosaic,
    sdfi_satellite_orthophotos,
    sdfi_topo_map,
)
from qgreenland.models.config.layer import Layer, LayerInput

blue_marble_layer = Layer(
    id="blue_marble_shaded_relief_bathymetry",
    title="Blue Marble shaded relief and Bathymetry (500m)",
    description=(
        """Blue Marble (August 2004, Shaded Relief and Bathymetry).

        The MODIS Blue Marble, Next Generation layer with Shaded Relief and
        Bathymetry is a cloud free, true color composite of MODIS imagery from
        August 2004 including shaded relief and bathymetry in the water bodies.

        The MODIS Blue Marble, Next Generation is a static product created with data
        from 2004 from the MODIS instrument on board the Terra satellite. The image
        resolution is 500 m. It can be viewed in Worldview/Global Imagery Browse
        Services (GIBS). Images for January – December 2004 can be downloaded from
        NASA’s Visible Earth.

        References: NASA Earth Observatory - Blue Marble
        [https://earthobservatory.nasa.gov/features/BlueMarble]; NASA Earth
        Observations - Blue Marble
        [https://neo.gsfc.nasa.gov/view.php?datasetId=BlueMarbleNG-TB]; NASA
        Earth Observations - Blue Marble: Next Generation+Topography and
        Bathymetry
        [https://neo.gsfc.nasa.gov/view.php?datasetId=BlueMarbleNG-TB]."""
    ),
    tags=["online"],
    input=LayerInput(
        dataset=gibs,
        asset=gibs.assets["only"],
    ),
)


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

sdfi_topo_map_layer = Layer(
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


sdfi_satellite_orthophotos_layer = Layer(
    id="sdfi_satellite_orthophotos",
    title="Satellite orthophoto mosaic (10-0.2m)",
    description=(
        """Orthophoto mosaic from Sentinel2 (10m), Spot (1.6m), and Asiaq
        (0.2m). Displayed data depends on availability and zoom level.

        Sentinel2 (10m): The Sentinel 2 satellites record images for approx. 10
        m resolution. The images are ortho-created. For the orthorectification
        of the images, either the height model GLOBE (1km) or SRTM (30 m) is
        used. The image material consists of images taken in August 2019 and
        2020.  The geometric accuracy is within 1-2 pixels (10-20 m). In some
        places, offsets of up to 10 pixels (100 m) can occur.

        Spot (1.6m): Orthophotos calculated from SPOT6/7 satellite images. The
        SPOT satellites record images for approx. 1.5 m resolution. The images
        are orthorectified so that they are accurate and resampled to 1.6 m. The
        height model WorldDEM4ortho (Airbus' own DEM) is used for the
        orthorectification of the images. The image material consists of
        approx. 75% of the coverage of images taken in the summer of 2020. About
        25% of the coverage dates to 2016, while some recordings are from 2013
        and 2014.  The geometric accuracy is expected to be better than 10
        pixels, which corresponds to 16 m.

        Asiaq (0.2m): orthophoto from residences calculated from aerial #
        photography.  The images are recorded images in approx. 20cm
        resolution. Some areas in 10cm.  For additional facts about origin and
        data quality, refer to Asiaq [https://www.asiaq-greenlandsurvey.gl/],
        who was responsible for the collection.
        """
    ),
    tags=["online"],
    input=LayerInput(
        dataset=sdfi_satellite_orthophotos,
        asset=sdfi_satellite_orthophotos.assets["only"],
    ),
)


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
