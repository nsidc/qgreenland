from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

gc_net_promice_stations = Dataset(
    id="gc_net_promice_stations",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://dataverse.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/FK2/IW73UU/AQMRYQ",
            ],
        ),
    ],
    metadata={
        "title": "PROMICE and GC-Net automated weather station data in Greenland",
        "abstract": (
            """In 2007, Denmark launched the Programme for Monitoring of the
            Greenland Ice Sheet (PROMICE) to assess changes in the mass balance
            of the ice sheet. The two major contributors to the ice sheet mass
            loss are surface melt and a larger production of icebergs through
            faster ice flow. PROMICE is focused on both processes. Ice movement
            and discharge is tracked by satellites and GPSs. The surface mass
            balance is monitored by a network of weather stations in the melt
            zone of the ice sheet, providing ground truth data to calibrate mass
            budget models.

            The Greenland Climate Network (GC-Net) was established in 1995 by
            Prof. Konrad Steffen at CIRES, to obtain knowledge of the mass gain
            and climatology of the ice sheet. The programme was funded by the
            USA until 2020, at which point Denmark assumed responsibility for
            the operation and maintenance of the weather station network. The
            snowfall and climatology are monitored by a network of weather
            stations in the accumulation zone of the ice sheet, supplemented by
            satellite-derived data products.

            Together, the two monitoring programmes deliver data about the mass
            balance of the Greenland ice sheet in near real-time.

            Data from the Programme for Monitoring of the Greenland Ice Sheet
            (PROMICE) are provided by the Geological Survey of Denmark and
            Greenland (GEUS) at http://www.promice.dk. They include sites
            financially supported by the Glaciobasis programme as part of
            Greenland Ecosystem Monitoring (https://g-e-m.dk/), maintained by
            GEUS (ZAK, LYN) and by Asiaq Greenland Survey (NUK_K). The WEG
            stations are paid for and maintained by the University of Graz.

            See https://github.com/GEUS-Glaciology-and-Climate/pypromice for how
            we make the data product.

            Related publication:

            Fausto, R. S., van As, D., Mankoff, K. D., Vandecrux, B., Citterio,
            M., Ahlstrøm, A. P., Andersen, S. B., Colgan, W., Karlsson, N. B.,
            Kjeldsen, K. K., Korsgaard, N. J., Larsen, S. H., Nielsen, S.,
            Pedersen, A. Ø., Shields, C. L., Solgaard, A. M., and Box, J. E.:
            Programme for Monitoring of the Greenland Ice Sheet (PROMICE)
            automatic weather station data, Earth Syst. Sci. Data, 13,
            3819–3845, https://doi.org/10.5194/essd-13-3819-2021, 2021.

            Additional data:

            To download data related to PROMICE and GC-Net, including historical
            weather station data, see
            https://dataverse.geus.dk/dataverse/PROMICE."""
        ),
        "citation": {
            "text": (
                """How, P., Abermann, J., Ahlstrøm, A.P., Andersen, S.B., Box,
J.E., Citterio, M., Colgan, W.T., Fausto, R., Karlsson, N.B., Jakobsen, J.,
Langley, K., Larsen, S.H., Mankoff, K.D., Pedersen, A.Ø., Rutishauser, A.,
Shields, C.L., Solgaard, A.M., van As, D., Vandecrux, B., Wright, P.J., 2022,
"PROMICE and GC-Net automated weather station data in Greenland",
https://doi.org/10.22008/FK2/IW73UU, GEUS Dataverse.

Date accessed: {{date_accessed}}."""
            ),
            "url": "https://dataverse.geus.dk/dataset.xhtml?persistentId=doi:10.22008/FK2/IW73UU",
        },
    },
)
