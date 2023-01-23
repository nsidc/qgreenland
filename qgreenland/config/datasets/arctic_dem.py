from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

arctic_dem = Dataset(
    id="arctic_dem",
    assets=[
        HttpAsset(
            id="1km",
            urls=[
                "http://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/1km/arcticdem_mosaic_1km_v3.0.tif",
            ],
        ),
        HttpAsset(
            id="500m",
            urls=[
                "http://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/500m/arcticdem_mosaic_500m_v3.0.tif",
            ],
        ),
        HttpAsset(
            id="100m",
            # This shouldn't be necessary?
            verify_tls=False,
            urls=[
                "https://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/100m/arcticdem_mosaic_100m_v3.0.tif",
            ],
        ),
    ],
    metadata={
        "title": "Arctic DEM (1km mosaic)",
        "abstract": (
            """ArcticDEM is an NGA-NSF public-private initiative to
            automatically produce a high-resolution, high quality, digital
            surface model (DSM) of the Arctic using optical stereo imagery,
            high-performance computing, and open source photogrammetry
            software."""
        ),
        "citation": {
            "text": (
                """Data provided by the Polar Geospatial Center. Porter, Claire;
                Morin, Paul; Howat, Ian; Noh, Myoung-Jon; Bates, Brian;
                Peterman, Kenneth; Keesey, Scott; Schlenk, Matthew; Gardiner,
                Judith; Tomko, Karen; Willis, Michael; Kelleher, Cole; Cloutier,
                Michael; Husby, Eric; Foga, Steven; Nakamura, Hitomi; Platson,
                Melisa; Wethington, Michael, Jr.; Williamson, Cathleen; Bauer,
                Gregory; Enos, Jeremy; Arnold, Galen; Kramer, William; Becker,
                Peter; Doshi, Abhijit; D’Souza, Cristelle; Cummens, Pat;
                Laurier, Fabien; Bojesen, Mikkel, 2018, “ArcticDEM”,
                https://doi.org/10.7910/DVN/OHHUKH, Harvard Dataverse, V1,
                2020-01-23"""
            ),
            "url": "https://www.pgc.umn.edu/data/arcticdem/",
        },
    },
)
