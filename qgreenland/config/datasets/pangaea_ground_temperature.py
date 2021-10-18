from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


pangaea_ground_temperature = ConfigDataset(
    id='pangaea_ground_temperature',
    assets=[
        ConfigDatasetHttpAsset(
            id='25km',
            urls=[
                'http://store.pangaea.de/Publications/ObuJ-etal_2018/UiO_PEX_5.0_20181127_2000_2016_25km.nc',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='10km',
            urls=[
                'http://store.pangaea.de/Publications/ObuJ-etal_2018/UiO_PEX_5.0_20181127_2000_2016_10km.nc',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='5km',
            urls=[
                'http://store.pangaea.de/Publications/ObuJ-etal_2018/UiO_PEX_5.0_20181127_2000_2016_5km.nc',
            ],
        ),
    ],
    metadata={
        'title': 'Ground Temperature Map, 2000-2016, Northern Hemisphere Permafrost',
        'abstract': (
            """Original data information: The product provides modeled mean
            annual ground temperatures (MAGT) at the top of the permafrost for
            the Northern Hemisphere at 1 km spatial resolution. Permafrost
            probability (fraction values from 0 to 1) is assigned to each grid
            cell with MAGT < 0°C. Based on its permafrost probability each grid
            cell is classified as continuous, discontinuous and sporadic
            permafrost. The processing extent covers exposed land areas of the
            Northern Hemisphere down to 25° latitude. The mean MAGT was
            validated with GTN-P and TSP borehole ground temperature data and
            yielded a RMS of 2.0 °C. According to the results, permafrost (MAGT
            < 0 °C) covers 15 % of exposed land of the Northern Hemisphere.

            The map was produced within the project ESA Data User Element
            GlobPermafrost.

            QGreenland displays data at 10 km resolution.

            Dataset update: 2019-04-01"""
        ),
        'citation': {
            'text': (
                """Obu, Jaroslav; Westermann, Sebastian; Kääb, Andreas; Bartsch,
                Annett (2018): Ground Temperature Map, 2000-2016, Northern
                Hemisphere Permafrost. Alfred Wegener Institute, Helmholtz
                Centre for Polar and Marine Research, Bremerhaven, PANGAEA"""
            ),
            'url': 'https://doi.org/10.1594/PANGAEA.888600',
        },
    },
)
