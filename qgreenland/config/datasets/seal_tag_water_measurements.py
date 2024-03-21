from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

dataset = Dataset(
    id="seal_tag_measurements",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f",
            ],
        ),
    ],
    metadata={
        "title": "Water temperature, salinity, and position-geographic data taken from seal tags, in coastal Greenland from 2010-08-31 to 2012-05-14",
        "abstract": (
            """This project involves a marine-mammal sensor-tagging
        approach that will allow for sustained oceanographic observations along
        the periphery of the Greenland Ice Sheet. This effort is motivated by a
        successful pilot project involving ringed seals in two Greenland fjords
        this past summer. The pilot proved the viability of the technique, which
        makes use of ringed seals who spend the majority of their time in such
        fjords and who may be appropriately equipped with integrated,
        location-tracking, CTD, and satellite communication instrumentation. The
        observations, which will be collected in partnership with colleagues at
        the Greenland Institute of Natural Resources, will be archived in
        national data bases, on a project website, and made widely available to
        others in near real-time. This project will address a currently missing,
        critical component of the Arctic Observing Network, namely observations
        of ocean temperatures and salinities along the periphery of the
        Greenland Ice Sheet. The methodology will lead to a practical,
        sustainable data stream for hydrographic properties in the notoriously
        difficult to access regions of the Greenland inner fjords, thus further
        filling out the overall Arctic Observing Network data portfolio. Such
        observations are needed to develop improved physics that can
        subsequently be directly used in IPCC class, coupled climate models. The
        data collection will also be of immense value to researchers studying
        the behavior of the ringed seals in Greenland. Virtually no behavioral
        data exists for these seals in the ice-ocean fjords, and the project
        data can be used to learn about the habitat and distribution of the
        seals, and ultimately of their possible vulnerability to climate
        change."""
        ),
        "citation": {
            "text": (
                """David Holland. (2018). Water temperature, salinity, and
            position-geographic data taken from seal tags, in coastal Greenland
            from 2010-08-31 to 2012-05-14. Arctic Data
            Center. urn:uuid:1f3f702f-9594-4293-8cbd-07932e54e8ed."""
            ),
            "url": "https://arcticdata.io/catalog/view/urn%3Auuid%3A1f3f702f-9594-4293-8cbd-07932e54e8ed",
        },
    },
)
