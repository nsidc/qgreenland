from qgreenland.models.config.asset import ConfigDatasetManualAsset
from qgreenland.models.config.dataset import ConfigDataset


danish_agency_for_data_supply_and_efficiency_gtk_topo_map = ConfigDataset(
    id='danish_agency_for_data_supply_and_efficiency_gtk_topo_map',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions=(
                """Downloaded through the The Danish Agency for Map Supply and
                Efficiency's website on 2020-12-17. User registration is
                required. Once the ordered data were delivered (as a zipfile),
                they were extracted and a mosaic was created of the 500m version
                of the data via the `scripts/danish_agency_for_data_supply_and_e
                fficiency_gtk_topo_map/preprocess.sh` script."""
            ),
        ),
    ],
    metadata={
        'title': "Greenland's Topographical Map 1:500,000",
        'abstract': (
            """Greenland's topographical map work is a collection of Greenland
            maps in different dimensions. The original product contains the
            following target ratios: 1:250,000, 1:500,000 and 1:2.5 million."""
        ),
        'citation': {
            'text': (
                """Contains data from Styrelsen for dataforsyning og
                effektivisering. Accessed {{date_accessed}}."""
            ),
            'url': 'https://download.kortforsyningen.dk/content/gr%C3%B8nlands-topografiske-kortv%C3%A6rk',
        },
    },
)
