from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

circumpolar_layer_monitoring = Dataset(
    id="circumpolar_layer_monitoring",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://www2.gwu.edu/~calm/data/CALM_Sites_wData.7z",
            ],
        ),
    ],
    metadata={
        "title": "Circumpolar Active Layer Monitoring Network-CALM: Long-Term Observations of the Climate-Active Layer-Permafrost System",
        "abstract": (
            """The primary goal of the Circumpolar Active Layer Monitoring
            (CALM) program is to observe the response of the active layer and
            near-surface permafrost to climate change over long (multi-decadal)
            time scales. The CALM observational network, established in the
            1990s, observes the long-term response of the active layer and
            near-surface permafrost to changes and variations in climate at more
            than 200 sites in both hemispheres. CALM currently has participants
            from 15 countries. Majority of sites measure active-layer thickness
            on grids ranging from 1 ha to 1 km², and observe soil
            temperatures. Most sites in the CALM network are located in Arctic
            and Subarctic lowlands. Southern Hemisphere component (CALM-South)
            is being organized and currently includes sites in Antarctic and
            South America. The broader impacts of this project are derived from
            the hypothesis that widespread, systematic changes in the thickness
            of the active layer could have profound effects on the flux of
            greenhouse gases, on the human infrastructure in cold regions, and
            on landscape processes. It is therefore critical that observational
            and analytical procedures continue over decadal periods to assess
            trends and detect cumulative, long-term changes.

            The CALM program began in 1991. It was initially affiliated with the
            International Tundra Experiment and has been supported independently and
            continuously since 1998 through grants from the U.S. National Science
            Foundation*. CALM is funded by the NSF Project OPP-1836377."""
        ),
        "citation": {
            "text": ("""TODO..."""),
            "url": "https://www2.gwu.edu/~calm/data/north.htm",
        },
    },
)
