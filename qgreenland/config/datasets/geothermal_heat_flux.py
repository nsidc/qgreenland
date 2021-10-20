from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


geothermal_heat_flux = ConfigDataset(
    id='geothermal_heat_flux',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://ads.nipr.ac.jp/portal/kiwa/DataDownloadDownload.action?mode=single&path=ADS%3AArCS-T2%3AA20180227-001%3A2.00%3A%2FArCS-T2%2FA20180227-001%2Fv200%2Fdataset%2FGHF_Greenland_Ver2.0_GridEPSG3413_05km.nc&downloads=ADS%3AArCS-T2%3AA20180227-001%3A2.00%3A%2FArCS-T2%2FA20180227-001%2Fv200%2Fdataset%2FGHF_Greenland_Ver2.0_GridEPSG3413_05km.nc',
            ],
        ),
    ],
    metadata={
        'title': 'Geothermal heat flux distribution for the Greenland ice sheet, derived by combining a global representation and information from deep ice cores',
        'abstract': (
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
        'citation': {
            'text': (
                """Polar Data Journal, 3, 22-36.
                https://doi.org/10.20575/00000006"""
            ),
            'url': 'https://doi.org/10.20575/00000006',
        },
    },
)
