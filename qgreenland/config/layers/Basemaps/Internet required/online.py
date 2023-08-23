from qgreenland.config.datasets.online import (
    gibs,
    sdfi_topo_map,
)
from qgreenland.models.config.layer import Layer, LayerInput

sdfi_topo_map_layer = Layer(
    id="sdfi_topo_map",
    title="Topographic map of Greenland",
    description=(
        """The Greenland vector data is based on commercial satellite images
            with a resolution of 0.5 m. The images are primarily from the summer
            months in the period from 2017 to 2021. Data is produced and quality
            assured according to ISO standards.

            Vector data from East Greenland are not
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

blue_marble_layer = Layer(
    id="blue_marble_shaded_relief_bathymetry",
    title="Blue Marble shaded relief and bathymetry (500m)",
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
