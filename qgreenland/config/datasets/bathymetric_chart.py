from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

bathymetric_chart = Dataset(
    id="bathymetric_chart",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://www.bodc.ac.uk/data/open_download/ibcao/ibcao_v4_2_400m_ice/cfnetcdf/",
            ],
        ),
    ],
    metadata={
        "title": "International Bathymetric Chart of the Arctic Ocean (IBCAO) V4.2",
        "abstract": (
            """The goal of the IBCAO initiative is to develop a digital database
            that contains all available bathymetric data north of 64° North, for
            use by mapmakers, researchers, institutions, and others whose work
            requires a detailed and accurate knowledge of the depth and the
            shape of the Arctic seabed.

            The IBCAO data set is included, as a regional compilation, in the
            global GEBCO grid
            [https://www.gebco.net/data_and_products/gridded_bathymetry_data/].

            Disclaimer information:

            The IBCAO V4.2 Grid, should NOT be used for navigation or for any
            other purpose involving safety at sea.

            The IBCAO V4.2 Grid is made available 'as is'. While every effort
            has been made to ensure reliability within the limits of present
            knowledge, the accuracy and completeness of The IBCAO V4.2 Grid
            cannot be guaranteed.

            No responsibility can be accepted by those involved in its creation
            or publication for any consequential loss, injury or damage arising
            from its use or for determining the fitness of The IBCAO V4.2 Grid
            for any particular use.

            The IBCAO V4.2 Grid is based on bathymetric data from many different
            sources of varying quality and coverage.

            As The IBCAO V4.2 Grid is an information product created by
            interpolation of measured data, the resolution of the IBCAO V4.2
            Grid may be significantly different to that of the resolution of the
            underlying measured data."""
        ),
        "citation": {
            "text": (
                """GEBCO Compilation Group (2023) GEBCO 2023 Grid
                (doi:10.5285/f98b053b-0cbc-6c23-e053-6c86abc0af7b)"""
            ),
            "url": "https://www.gebco.net/data_and_products/gridded_bathymetry_data/arctic_ocean/",
        },
    },
)

gebco_bathymetric_chart = Dataset(
    id="gebco_bathymetric_chart",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://www.bodc.ac.uk/data/open_download/gebco/gebco_2023/zip/",
            ],
        ),
    ],
    metadata={
        "title": "General Bathymetric Chart of the Oceans (GEBCO) Grid 2023",
        "abstract": (
            """The GEBCO_2023 Grid is a global terrain model for ocean and land,
            providing elevation data, in meters, on a 15 arc-second interval
            grid of 43200 rows x 86400 columns, giving 3,732,480,000 data
            points. The data values are pixel-centre registered i.e. they refer
            to elevations, in meters, at the centre of grid cells.

            The grid was published in April 2023 and is the fifth GEBCO grid
            developed through The Nippon Foundation-GEBCO Seabed 2030
            Project. This is a collaborative project between the Nippon
            Foundation of Japan and GEBCO. The Seabed 2030 Project aims to bring
            together all available bathymetric data to produce the definitive
            map of the world ocean floor and make it available to all."""
        ),
        "citation": {
            "text": (
                """GEBCO Compilation Group (2023) GEBCO 2023 Grid
                (doi:10.5285/f98b053b-0cbc-6c23-e053-6c86abc0af7b)"""
            ),
            "url": "https://www.gebco.net/data_and_products/gridded_bathymetry_data/",
        },
    },
)
