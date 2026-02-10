from qgreenland.models.config.asset import CmrAsset
from qgreenland.models.config.dataset import Dataset

bedmachine = Dataset(
    id="bedmachine",
    assets=[
        CmrAsset(
            id="only",
            granule_ur="BedMachineGreenland-v6.nc",
            collection_concept_id="C3903728370-NSIDC_CPRD",
        ),
    ],
    metadata={
        "title": "IceBridge BedMachine Greenland, Version 6",
        "abstract": """
This data set contains a bed topography/bathymetry map of Greenland based on
mass conservation, multi-beam data, and other techniques. It also includes
surface elevation and ice thickness data, as well as an ice/ocean/land mask.

As a condition of using these data, you must cite the use of this data set.
Such a practice gives credit to data set producers and advances principles of
transparency and reproducibility.

Morlighem, M. et al. (2025). IceBridge BedMachine Greenland. (IDBMG4, Version 6).
[Data Set]. Boulder, Colorado USA. NASA National Snow and Ice Data Center
Distributed Active Archive Center. https://doi.org/10.5067/6B6B225B8V2D.
[describe subset used if applicable]. Date Accessed 02-06-2026.
""",
        "citation": {
            "text": """
Morlighem, M. et al. (2025). IceBridge BedMachine Greenland. (IDBMG4, Version 6).
[Data Set]. Boulder, Colorado USA. NASA National Snow and Ice Data Center
Distributed Active Archive Center. https://doi.org/10.5067/6B6B225B8V2D.
[describe subset used if applicable]. Date Accessed 02-06-2026.
""",
            "url": "https://doi.org/10.5067/6B6B225B8V2D",
        },
    },
)
