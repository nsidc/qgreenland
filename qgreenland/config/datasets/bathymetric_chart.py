from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

bathymetric_chart = Dataset(
    id="bathymetric_chart",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://www.bodc.ac.uk/data/open_download/ibcao/ibcao_v4_400m_ice/cfnetcdf/",
            ],
        ),
    ],
    metadata={
        "title": "Bathymetric Chart of the Arctic Ocean (IBCAO)",
        "abstract": (
            """The goal of the IBCAO initiative is to develop a digital database
            that contains all available bathymetric data north of 64° North, for
            use by mapmakers, researchers, institutions, and others whose work
            requires a detailed and accurate knowledge of the depth and the
            shape of the Arctic seabed."""
        ),
        "citation": {
            "text": (
                """GEBCO Compilation Group (2020) GEBCO 2020 Grid
                (doi:10.5285/a29c5465-b138-234d-e053-6c86abc040b9)"""
            ),
            "url": "https://www.gebco.net/data_and_products/gridded_bathymetry_data/arctic_ocean/",
        },
    },
)
