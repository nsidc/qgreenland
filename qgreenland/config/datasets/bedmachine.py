from qgreenland.models.config.asset import CmrAsset
from qgreenland.models.config.dataset import Dataset

bedmachine = Dataset(
    id="bedmachine",
    assets=[
        CmrAsset(
            id="only",
            granule_ur="SC:IDBMG4.005:244470242",
            collection_concept_id="C2420522159-NSIDC_ECS",
        ),
    ],
    metadata={
        "title": "IceBridge BedMachine Greenland, Version 5",
        "abstract": """
This data set contains a bed topography/bathymetry map of Greenland based on
mass conservation, multi-beam data, and other techniques. It also includes
surface elevation and ice thickness data, as well as an ice/ocean/land mask.

As a condition of using these data, we request that you acknowledge the
author(s) of this data set by referencing the following peer-reviewed
publication.

Morlighem, M., C. Williams, E. Rignot, L. An, J. E. Arndt, J. Bamber,
G. Catania, N. Chauché, J. A. Dowdeswell, B. Dorschel, I. Fenty, K. Hogan,
I. Howat, A. Hubbard, M. Jakobsson, T. M. Jordan, K. K. Kjeldsen, R. Millan,
L. Mayer, J. Mouginot, B. Noël, C. O'Cofaigh, S. J. Palmer, S. Rysgaard,
H. Seroussi, M. J. Siegert, P. Slabon, F. Straneo, M. R. van den Broeke,
W. Weinrebe, M. Wood, and K. Zinglersen. 2017. BedMachine v3: Complete bed
topography and ocean bathymetry mapping of Greenland from multi-beam echo
sounding combined with mass conservation, Geophysical Research
Letters. 44. . https://doi.org/10.1002/2017GL074954 .
""",
        "citation": {
            "text": """
Morlighem, M. et al. (2022). IceBridge BedMachine Greenland, Version 5 [Data
Set]. Boulder, Colorado USA. NASA National Snow and Ice Data Center Distributed
Active Archive Center. https://doi.org/10.5067/GMEVBWFLWA7X. Date Accessed
06-08-2023.
""",
            "url": "https://doi.org/10.5067/GMEVBWFLWA7X",
        },
    },
)
