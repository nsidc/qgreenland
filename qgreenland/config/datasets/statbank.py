from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

statbank = Dataset(
    id="statbank",
    assets=[
        HttpAsset(
            id="municipalities_population",
            # This URL returns a csv file `BEXSTB.csv` that has data for Jan 1, 1977-present
            urls=["https://bank.stat.gl:443/sq/e38caec2-e806-4a9d-9a01-59f021282b56"],
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
