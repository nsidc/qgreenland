from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

geus_cryo_seismic_events = Dataset(
    id="geus_cryo_seismic_events",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://seis.geus.net/quakes/cryo.lis",
            ],
        ),
    ],
    metadata={
        "title": "Cryo-generated Seismic Events in Greenland",
        "abstract": (
            """Parametric data from cryo-generated seismic events in Greenland,
            detected, processed and analysed at the Geological Survey of Denmark
            and Greenland – GEUS, using data from the earthquake monitoring
            network. Daily updates of the data is available via the URL
            https://seis.geus.net/quakes/cryo.lis for a simple CSV listing of
            event time and location, given by date and UTC time and latitude and
            longitude (WGS 84). Or via the URL
            https://seis.geus.net/quakes/cryo.nor for the complete set of
            parametric data available in the event database at GEUS. Here the
            data are given in the Nordic format, described in appendix A of the
            SEISAN manual (Ottemöller et al. 2021). REF: Ottemöller, L., Voss,
            P.H. and Havskov J. (2021). SEISAN Earthquake Analysis Software for
            Windows, Solaris, Linux and Macosx, Version 12.0. 607 pp. University
            of Bergen. ISBN 978-82-8088-501-2. (2022-03-18)."""
        ),
        "citation": {
            "text": (
                """Voss, Peter H. and Dahl-Jensen, Trine and Larsen, Tine B. and Rinds, Nicoali, 2022,
                "Cryo-generated Seismic Events in Greenland, V1", GEUS Dataverse.

                Date accessed: {{date_accessed}}."""
            ),
            "url": "https://doi.org/10.22008/FK2/ABMBLO",
        },
    },
)
