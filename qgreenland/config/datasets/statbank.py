from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

statbank = Dataset(
    id="statbank",
    assets=[
        # This asset from the "Population in Municipalities January 1st 1977-2026" table.
        HttpAsset(
            id="municipalities_population",
            # This URL returns a csv file `BEXSTB.csv` that has data for Jan 1, 1977-present
            urls=["https://bank.stat.gl:443/sq/e38caec2-e806-4a9d-9a01-59f021282b56"],
        ),
        # This asset from the "Population in Localities January 1st by locality and time" table.
        HttpAsset(
            id="localities_population",
            # This URL returns a csv file `BEXSTD.csv` that has data for Jan 1, 1977-present
            urls=["https://bank.stat.gl:443/sq/fbea8c31-dac7-420f-aa7d-dd93ea59f91e"],
        ),
        # This asset from the "Population in Localities January 1st by locality and time" table.
        HttpAsset(
            id="international_passengers",
            # This URL returns a csv file `TUXPAX.csv` that has data for Jan 2008-present
            urls=["https://bank.stat.gl:443/sq/f93c6266-8b3e-4bc1-8bc7-71028d558456"],
        ),
        # This asset from the "Number of cruise passengers for each harbour by month, port and time" table.
        HttpAsset(
            id="cruise_passengers",
            # This URL returns a csv file `TUXKRH.csv` that has data for 2015-present
            urls=["https://bank.stat.gl:443/sq/d3c43015-ce8f-4934-ae3f-0a3b9761f8b7"],
        ),
    ],
    metadata={
        "title": "Statistics Greenland",
        # TODO: have team review abstract
        "abstract": (
            """You'll find all tables published by Statistics Greenland in our
            StatBank. The tables are updated in parallel with publications on
            our website. We aim to publish all tables in Greenlandic, Danish and
            English.

            Our StatBank is controlled by the program PX-Web, which for 25 years
            has been developed by the Swedish National Statistics Office (
            www.SCB.se ) in collaboration with many national statistical
            offices. This means that the methods, you as a user of our StatBank
            acquires, can be used to find statistics about many other countries,
            including Sweden, Finland, Norway, Iceland, the Faroe Islands,
            Aaland, Denmark,."""
        ),
        "citation": {
            # TODO: have team review citation
            "text": ("""Statistics Greenland. {{date_accessed}}"""),
            "url": "https://stat.gl/default.asp?lang=en",
        },
    },
)
