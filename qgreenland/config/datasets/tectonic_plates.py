from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

tectonic_plates = Dataset(
    id="tectonic_plates",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://github.com/fraxen/tectonicplates/archive/339b0c5.zip",
            ],
        ),
    ],
    metadata={
        "title": "World tectonic plates and boundaries",
        "abstract": (
            """As per data source - This dataset is a conversion of the dataset
            originally published in the paper 'An updated digital model of plate
            boundaries' by Peter Bird (Geochemistry Geophysics Geosystems, 4(3),
            1027, doi:10.1029/2001GC000252
            [http://scholar.google.se/scholar?cluster=1268723667321132798],
            2003). To bring this dataset into the modern age, the original data
            has been parsed, cleaned, and verified using ArcGIS 10.2 and
            converted to shape files. The dataset presents tectonic plates and
            their boundaries, and in addition orogens and information about the
            boundaries. The data is useful for geological applications, analysis
            and education, and should be easy to use in any modern GIS software
            application. For information on the fields and values, please refer
            to the [original](http://peterbird.name/oldFTP/PB2002/2001GC000252_r
            eadme.txt) documentation and the scientific article.

            Dataset credit should acknowledge Hugo Ahlenius, Peter Bird, and
            Nordpil, with an additional suggested citation included."""
        ),
        "citation": {
            "text": (
                """Ahlenius, H. (2014). World tectonic plates and boundaries.
                Data available from https://github.com/fraxen/tectonicplates."""
            ),
            "url": "https://github.com/fraxen/tectonicplates",
        },
    },
)
