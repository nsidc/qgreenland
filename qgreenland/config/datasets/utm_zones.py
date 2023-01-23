from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

utm_zones = Dataset(
    id="utm_zones",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "http://sandbox.idre.ucla.edu/mapshare/data/world/data/utmzone.zip",
            ],
        ),
    ],
    metadata={
        "title": "World UTM Zones",
        "abstract": (
            """World UTM Zones represents the Universal Transverse Mercator
            (UTM) zones of the world. The polygons represent the Universal
            Transverse Mercator (UTM) zones, which lie between 84 degrees North
            and 80 degrees South latitude. With few exceptions, they divide the
            world into sixty zones, each of which is six degrees of longitude
            wide. The zones are numbered from 1 through 60 eastward from 180
            degrees West longitude. The zone characters designate rows that are
            8 degrees of latitude high extending north and south from the
            equator with the exception of the northern-most row which is 12
            degrees high."""
        ),
        # Is this citation good enough? Find another source?
        "citation": {
            "text": ("""ESRI Data & Maps. 2015."""),
            "url": "https://apps.gis.ucla.edu/geodata/dataset/world_utm_zones",
        },
    },
)
