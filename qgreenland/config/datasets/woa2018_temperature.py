from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


BASE_URL = 'https://www.ncei.noaa.gov/thredds-ocean/fileServer/ncei/woa/temperature/decav'

woa2018_temperature = ConfigDataset(
    id='woa2018_temperature',
    assets=[
        ConfigDatasetHttpAsset(
            id='seasonal_winter',
            urls=[
                f'{BASE_URL}/0.25/woa18_decav_t13_04.nc',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='seasonal_summer',
            urls=[
                f'{BASE_URL}/0.25/woa18_decav_t15_04.nc',
            ],
        ),
    ],
    metadata={
        'title': 'WORLD OCEAN ATLAS 2018 Volume 1: Temperature',
        'abstract': (
            """From the World Ocean Atlas: This atlas consists of a description
            of data analysis procedures and horizontal maps of climatological
            distribution fields of temperature at selected standard depth levels
            of the World Ocean on one-degree and quarter-degree
            latitude-longitude grids.  The aim of the maps is to illustrate
            large-scale characteristics of the distribution of ocean
            temperature.  The fields used to generate these climatological maps
            were computed by objective analysis of all scientifically
            quality-controlled historical temperature data in the World Ocean
            Database 2018.  Maps are presented for climatological composite
            periods (annual, seasonal, monthly, seasonal and monthly difference
            fields from the annual mean field, and the number of observations)
            at 102 standard depths."""
        ),
        'citation': {
            'text': (
                """Locarnini, R. A., A. V. Mishonov, O. K. Baranova, T. P.
                Boyer, M. M. Zweng, H. E. Garcia, J. R. Reagan, D. Seidov, K. W.
                Weathers, C. R. Paver, I.  V. Smolyar, 2019: World Ocean Atlas
                2018, Volume 1: Temperature.  A. V.  Mishonov, Technical Ed.,
                NOAA Atlas NESDIS 81"""
            ),
            'url': 'https://data.nodc.noaa.gov/woa/WOA18/DOC/woa18_vol1.pdf',
        },
    },
)
