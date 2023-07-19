from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

gtn_permafrost = Dataset(
    id="gtn_permafrost",
    assets=[
        HttpAsset(
            id="boreholes",
            urls=[
                "http://flatey.arcticportal.org:8080/geoserver/page21/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=page21:tsp&maxFeatures=3000&outputFormat=CSV",
            ],
        ),
        HttpAsset(
            id="calm_sites",
            urls=[
                "https://gtnp.arcticportal.org/images/downloads/calm.csv",
            ],
        ),
    ],
    metadata={
        "title": "Global Terrestrial Network for Permafrost (GTN-P)",
        "abstract": (
            """The Global Terrestrial Network for Permafrost (GTN-P) is the
            primary international programme concerned with monitoring permafrost
            parameters. GTN-P was developed by the International Permafrost
            Association (IPA) under the Global Climate Observing System (GCOS)
            and the Global Terrestrial Observing Network (GTOS) in 1999, with
            the long term goal of obtaining a comprehensive view of the spatial
            structure, trends, and variability of changes in the active layer
            thickness and permafrost temperature."""
        ),
        "citation": {
            "text": (
                """Global Terrestrial Network for Permafrost. Date accessed: {{date_accessed}}."""
            ),
            "url": "https://gtnp.arcticportal.org/",
        },
    },
)
