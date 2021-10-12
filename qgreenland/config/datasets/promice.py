from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


gc_net_promice_stations = ConfigDataset(
    id='gc_net_promice_stations',
    assets=[
        ConfigDatasetHttpAsset(
            id='promice',
            urls=[
                'https://raw.githubusercontent.com/GEUS-PROMICE/map_GC-Net_PROMICE_kml/59455ddb50f7eeb1b8c5a5fdd7f80bfd548a0c92/input_data/PROMICE_info_from_GPS_data_2017-2018.csv',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='promice_former',
            urls=[
                'https://raw.githubusercontent.com/GEUS-PROMICE/map_GC-Net_PROMICE_kml/59455ddb50f7eeb1b8c5a5fdd7f80bfd548a0c92/input_data/PROMICE_info_from_GPS_data_2017-2018_former_sites.csv',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='gc_net',
            urls=[
                'https://raw.githubusercontent.com/GEUS-PROMICE/map_GC-Net_PROMICE_kml/59455ddb50f7eeb1b8c5a5fdd7f80bfd548a0c92/input_data/GCN%20info%20ca.2000.csv',
            ],
        ),
    ],
    metadata={
        'title': 'Map of GC-Net and PROMICE locations',
        'abstract': (
            """GitHub data description (creator: jasonebox): For PROMICE, I use
            a 2017-2018 average of station GPS data. I added an updated position
            for THU-U2. An improvement would be to have the .kml add the
            position date to the description and how it was obtained. For
            GC-Net, I use a table from Konrad Steffen. I added an updated
            position for PET ELA from 2016.

            Accuracy of positions is very important to avoid arriving in the
            field at an old location. In no cases, do I transcribe positions by
            hand as that can cause expensive problems not finding stations
            because of bad coordinates.

            QGreenland team notes - Source file indicating PROMICE GPS data from
            2017-2018 and GC-NET GPS data from 2000. See note from data creator
            above."""
        ),
        'citation': {
            'text': (
                """PROMICE, (2020). Map of GC-Net and PROMICE station locations.
                Web: https://github.com/GEUS-PROMICE. Date accessed:
                {{date_accessed}}."""
            ),
            'url': 'https://github.com/GEUS-PROMICE/map_GC-Net_PROMICE_kml/tree/59455ddb50f7eeb1b8c5a5fdd7f80bfd548a0c92',
        },
    },
)
