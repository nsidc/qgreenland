from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

soil_types = Dataset(
    id="soil_types",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "ftp://sidads.colorado.edu/pub/DATASETS/fgdc/ggd602_map_cryosols/ggd602_soils_greenland.dbf.gz",
                "ftp://sidads.colorado.edu/pub/DATASETS/fgdc/ggd602_map_cryosols/ggd602_soils_greenland.shp.gz",
                "ftp://sidads.colorado.edu/pub/DATASETS/fgdc/ggd602_map_cryosols/ggd602_soils_greenland.shx.gz",
            ],
        ),
    ],
    metadata={
        "title": "Northern Circumpolar Soils Map, Version 1",
        "abstract": (
            """The full data set consists of a circumpolar map of dominant soil
            characteristics, with a scale of 1:10,000,000, covering the United
            States, Canada, Greenland, Iceland, northern Europe, Russia,
            Mongolia, and Kazakhstan. The map was created using the Northern and
            Mid Latitude Soil Database. The map is in ESRI Shapefile format,
            consisting of 11 regional areas. Polygons have attributes that give
            the percentage polygon area that is a given soil type. The map shows
            the dominant soil of the spatial polygon unless the polygon is over
            90 percent rock or ice.  It also shows the proportion of polygon
            encompassed by the dominant soil or nonsoil. Soils include turbels,
            orthels, histels, histosols, mollisols, vertisols, aridisols,
            andisols, entisols, spodosols, inceptisols (and hapludolls),
            alfisols (cryalf and udalf), natric great groups, aqu-suborders,
            glaciers, and rocklands. QGreenland dispalys data for Greenland.
            Users can look to the source information for additional data."""
        ),
        "citation": {
            "text": (
                """Tarnocai, C., J. Kimble, D. Swanson, S. Goryachkin, Y. M.
                Naumov, V. Stolbovoi, B. Jakobsen, G. Broll, L. Montanarella, A.
                Arnoldussen, O. Arnalds, and M. Yli-Halla. 2002. Northern
                Circumpolar Soils Map, Version 1.  Greenland. Ottawa, Canada.
                Research Branch, Agriculture and Agri-Food Canada. doi:
                https://doi.org/. {{date_accessed}}"""
            ),
            "url": "https://nsidc.org/data/GGD602/versions/1",
        },
    },
)
