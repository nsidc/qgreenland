from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

ne_timezones = Dataset(
    id="ne_timezones",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_time_zones.zip",
            ],
        ),
    ],
    metadata={
        "title": "Timezones",
        "abstract": (
            """Time zones primarily derive from the Central Intelligence Agency
            map of Time Zones, downloaded from the World Factbook website May
            2012. Boundaries were adjusted to fit the Natural Earth line work at
            a scale of 1:10 million and to follow twelve nautical mile
            territorial sea boundary lines when running along coasts. Additional
            research was performed based on recent news to update several areas
            including the international dateline and time zone adjustments for
            Samoa and Tokelau and the discarding of daylight savings time in
            Russia.

            Data attributes include time offset from Coordinated Universal Time
            (UTC, aka “zulu” time) and map color codes for a 6-up and 8-up
            styling."""
        ),
        "citation": {
            "text": ("""Made with Natural Earth"""),
            "url": "https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md",
        },
    },
)
