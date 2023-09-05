from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.dataset import Dataset

arctic_dem_online_v4_1 = Dataset(
    id="arctic_dem_online_v4_1",
    assets=[
        OnlineAsset(
            id="only",
            provider="arcgismapserver",
            url=(
                "crs='EPSG:3413' crs='EPSG:3413' format='' layer='' "
                "url='https://overlord.pgc.umn.edu/arcgis/rest/services/elevation/"
                "pgc_arcticdem_mosaics_latest/ImageServer'"
            ),
        ),
    ],
    metadata={
        "title": "Arctic DEM",
        "abstract": (
            """ArcticDEM is an NGA-NSF public-private initiative to
            automatically produce a high-resolution, high quality, digital
            surface model (DSM) of the Arctic using optical stereo imagery,
            high-performance computing, and open source photogrammetry
            software."""
        ),
        "citation": {
            "text": (
                """Porter, C., Howat, I., Noh, M.J., Husby, E., Khuvis, S.,
Danish, E., Tomko, K., Gardiner, J., Negrete, A., Yadav, B., Klassen, J.,
Kelleher, C., Cloutier, M., Bakker, J., Enos, J., Arnold, G., Bauer, G., and
Morin, P., 2023, "ArcticDEM - Mosaics, Version 4.1",
https://doi.org/10.7910/DVN/3VDC4W"""
            ),
            "url": "https://www.pgc.umn.edu/data/arcticdem/",
        },
    },
)
