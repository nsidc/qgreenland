from qgreenland.config.datasets.online import gibs
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
