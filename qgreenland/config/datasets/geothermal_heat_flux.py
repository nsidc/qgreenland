from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

geothermal_heat_flux = Dataset(
    id="geothermal_heat_flux",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://ads.nipr.ac.jp/api/v1/metadata/A20180227-001/2.00/data/DATA?path=GHF_Greenland_Ver2.0_GridEPSG3413_05km.nc",
            ],
        ),
    ],
    metadata={
        "title": "Geothermal heat flux distribution for the Greenland ice sheet, derived by combining a global representation and information from deep ice cores",
        "abstract": (
            """The data present a distribution of the geothermal heat flux (GHF)
            for Greenland, which is an update of two earlier versions by Greve
            (2005, Ann. Glaciol. 42) and Greve and Herzfeld (2013, Ann. Glaciol.
            54). The GHF distribution is constructed in two steps. First, the
            global representation by Pollack et al. (1993, Rev. Geophys. 31) is
            scaled for the area of Greenland. Second, by means of a
            paleoclimatic simulation carried out with the ice sheet model
            SICOPOLIS, the GHF values for five deep ice core locations are
            modified such that observed and simulated basal temperatures match
            closely. The resulting GHF distribution generally features low
            values in the south and the north-west, whereas elevated values
            prevail in central North Greenland and towards the north-east. The
            original source data are provided as NetCDF files on two different
            grids (EPSG:3413 grid, Bamber grid) that have frequently been used
            in modelling studies of the Greenland ice sheet, and for the three
            different resolutions of 5 km, 10 km and 20 km."""
        ),
        "citation": {
            "text": (
                """Greve, R., 2018, Geothermal heat flux distribution for the
                Greenland ice sheet, derived by combining a global
                representation and information from deep ice cores, 2.00, Arctic
                Data archive System (ADS), Japan,
                http://doi.org/10.17592/001.2018022701"""
            ),
            "url": "http://doi.org/10.17592/001.2018022701",
        },
    },
)
