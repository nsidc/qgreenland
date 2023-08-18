from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

ice_cores = Dataset(
    id="ice_cores",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "http://gis.ncdc.noaa.gov/kml/paleo_icecore.kmz",
            ],
        ),
    ],
    metadata={
        "title": "Ice Cores",
        "abstract": (
            """Greenland ice core locations. Ice cores can provide records of
            past temperature, precipitation, atmospheric trace gases, and other
            aspects of climate and environment. Additional information is
            available in the 'description' attribute, including an ice core
            dataset URL. Data were accessed using the Google Earth Map Search
            Dataset. For details please see:
            http://www.ncdc.noaa.gov/paleo/icecore.html."""
        ),
        "citation": {
            "text": (
                """World Data Center (2020). Ice core locations. Download:
                http://gis.ncdc.noaa.gov/kml/paleo_icecore.kmz.
                {{date_accessed}}"""
            ),
            "url": "http://www.ncdc.noaa.gov/paleo/icecore.html",
        },
    },
)
