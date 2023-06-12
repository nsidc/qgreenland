from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

BASE_URL = "https://www.ncei.noaa.gov/thredds-ocean/fileServer/woa23/DATA/temperature/netcdf/decav91C0"

woa_temperature = Dataset(
    id="woa_temperature",
    assets=[
        HttpAsset(
            id="seasonal_winter",
            urls=[
                f"{BASE_URL}/0.25/woa23_decav91C0_t13_04.nc",
            ],
        ),
        HttpAsset(
            id="seasonal_summer",
            urls=[
                f"{BASE_URL}/0.25/woa23_decav91C0_t15_04.nc",
            ],
        ),
    ],
    metadata={
        "title": "World Ocean Atlas 2023, Volume 1: Temperature.",
        "abstract": (
            """The World Ocean Atlas (WOA) is a collection of objectively
            analyzed, quality controlled temperature, salinity, oxygen,
            phosphate, silicate, and nitrate means based on profile data from
            the World Ocean Database (WOD). It can be used to create boundary
            and/or initial conditions for a variety of ocean models, verify
            numerical simulations of the ocean, and corroborate satellite
            data."""
        ),
        "citation": {
            "text": (
                """Locarnini, R. A., O. K. Baranova, A. V. Mishonov,
                T. P. Boyer, J. R. Reagan, D. Dukhovskoy, D. Seidov,
                H. E. Garcia, C. Bouchard, S. Cross, C. R. Paver, and Z. Wang,
                2023. World Ocean Atlas 2023, Volume 1: Temperature. A. Mishonov
                Technical Ed. NOAA Atlas NESDIS (in preparation)."""
            ),
            "url": "https://www.ncei.noaa.gov/products/world-ocean-atlas",
        },
    },
)
