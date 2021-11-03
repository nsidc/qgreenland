from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


# The name of the `dataset` variable doesn't matter here.
dataset = ConfigDataset(
    # TODO: Fill in `your_dataset_id`. Be descriptive:
    id='geothermal_heat_flow',
    assets=[
        # This is interpolated data.
        # TODO: is there anything special about the upsampling done here?
        ConfigDatasetHttpAsset(
            id='10km_map',
            urls=['https://dataverse01.geus.dk/api/access/datafile/24634?gbrecs=true'],
        ),
        # This is the native resolution
        ConfigDatasetHttpAsset(
            id='55km_map',
            urls=['https://dataverse01.geus.dk/api/access/datafile/24633?gbrecs=true'],
        ),
    ],
    # TODO: Fill in _all_ metadata fields below:
    metadata={
        'title': 'Greenland Geothermal Heat Flow Database and Map',
        'abstract': (
            """Database of all geothermal heat flow measurements within 500 km
            of Greenland's coastline with self-consistent machine-learning
            geothermal heat flow map over all onshore and offshore areas.

            Related publication:

            Colgan, W., A. Wansing, K. Mankoff, M. Lösing, J. Hopper, K. Louden,
            J. Ebbing, F. Christiansen, T. Ingeman-Nielsen, L. Claesson
            Liljedahl, J. MacGregor, Á. Hjartarson, S. Bernstein, N. Karlsson,
            S. Fuchs, J. Hartikainen, J. Liakka, R. Fausto, D. Dahl-Jensen,
            A. Bjørk, J.-O. Naslund, F. Mørk, Y. Martos, N. Balling, T. Funck,
            K. Kjeldsen, D. Petersen, U. Gregersen, G. Dam, T. Nielsen, A. Khan
            and A. Løkkegaard. Greenland Geothermal Heat Flow Database and Map
            (Version 1). Earth Systems Science Data Discussions. under review."""
        ),
        'citation': {
            'text': (
                """Colgan, William; Wansing, Agnes, 2021, "Greenland Geothermal
                Heat Flow Database and Map",
                https://doi.org/10.22008/FK2/F9P03L, GEUS Dataverse, V1"""
            ),
            'url': 'https://doi.org/10.22008/FK2/F9P03L',
        },
    },
)
