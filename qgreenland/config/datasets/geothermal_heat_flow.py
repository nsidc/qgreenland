from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

geothermal_heat_flow = Dataset(
    id="geothermal_heat_flow",
    assets=[
        # A 10km map is also available but it is upsampled. This is the native
        # resolution
        HttpAsset(
            id="55km_map",
            urls=[
                "https://dataverse.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/FK2/F9P03L/FYNXIL"
            ],
        ),
        HttpAsset(
            id="heat_flow_measurements",
            urls=[
                "https://dataverse.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/FK2/F9P03L/V1IMQX"
            ],
        ),
    ],
    metadata={
        "title": "Greenland Geothermal Heat Flow Database and Map",
        "abstract": (
            """Database of all geothermal heat flow measurements within 500 km of
            Greenland's coastline with self-consistent machine-learning geothermal heat
            flow map over all onshore and offshore areas.

            Related publication:

            Colgan, W., A. Wansing, K. Mankoff, M. Lösing, J. Hopper, K. Louden, J.
            Ebbing, F. Christiansen, T. Ingeman-Nielsen, L. Claesson Liljedahl, J.
            MacGregor, Á. Hjartarson, S. Bernstein, N. Karlsson, S. Fuchs, J.
            Hartikainen, J. Liakka, R. Fausto, D. Dahl-Jensen, A. Bjørk, J.-O. Naslund,
            F. Mørk, Y. Martos, N. Balling, T. Funck, K. Kjeldsen, D. Petersen, U.
            Gregersen, G. Dam, T. Nielsen, S. Khan and A. Løkkegaard. Greenland
            Geothermal Heat Flow Database and Map (Version 1). 2022. Earth Systems
            Science Data. 14: 2209–2238. doi: 10.5194/essd-14-2209-2022.

            We compile and analyze all available geothermal heat flow measurements
            collected in and around Greenland into a new database of 419 sites and
            generate an accompanying spatial map. This database includes 290 sites
            previously reported by the International Heat Flow Commission (IHFC), for
            which we now standardize measurement and metadata quality. This database
            also includes 129 new sites, which have not been previously reported by the
            IHFC. These new sites consist of 88 offshore measurements and 41 onshore
            measurements, of which 24 are subglacial. We employ machine learning to
            synthesize these in situ measurements into a gridded geothermal heat flow
            model that is consistent across both continental and marine areas in and
            around Greenland. This model has a native horizontal resolution of 55 km. In
            comparison to five existing Greenland geothermal heat flow models, our model
            has the lowest mean geothermal heat flow for Greenland onshore areas. Our
            modeled heat flow in central North Greenland is highly sensitive to whether
            the NGRIP (North GReenland Ice core Project) elevated heat flow anomaly is
            included in the training dataset. Our model's most distinctive spatial
            feature is pronounced low geothermal heat flow (< 40 mW m−2) across the
            North Atlantic Craton of southern Greenland. Crucially, our model does not
            show an area of elevated heat flow that might be interpreted as remnant from
            the Icelandic plume track. Finally, we discuss the substantial influence of
            paleoclimatic and other corrections on geothermal heat flow measurements in
            Greenland. The in situ measurement database and gridded heat flow model, as
            well as other supporting materials, are freely available from the GEUS
            Dataverse (https://doi.org/10.22008/FK2/F9P03L; Colgan and Wansing, 2021).
            """
        ),
        "citation": {
            "text": (
                """Colgan, William; Wansing, Agnes, 2021, "Greenland Geothermal
                Heat Flow Database and Map",
                https://doi.org/10.22008/FK2/F9P03L, GEUS Dataverse, V2"""
            ),
            "url": "https://doi.org/10.22008/FK2/F9P03L",
        },
    },
)
