from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

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
