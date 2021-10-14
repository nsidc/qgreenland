from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


glims = ConfigDataset(
    id='glims',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'http://www.glims.org/download/glims_db_20200630.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Global Land Ice Measurements from Space glacier database',
        'abstract': (
            """Global Land Ice Measurements from Space (GLIMS) is an
            international initiative with the goal of repeatedly surveying the
            world's estimated 200,000 glaciers. GLIMS is characterizing and
            categorizing the many Greenland peripheral glaciers and ice caps,
            rather than the contiguous ice sheet region.

            The GLIMS initiative has created a unique glacier inventory, storing
            information about the extent and rates of change of all the world's
            mountain glaciers and ice caps. GLIMS uses data collected by the
            Advanced Spaceborne Thermal Emission and Reflection Radiometer
            (ASTER) instrument aboard the Terra satellite and the LANDSAT series
            of satellites, along with historical observations. The GLIMS Glacier
            Database was built up from data contributions from many
            glaciological institutions, which are managed by Regional
            Coordinators, who coordinate the production of glacier mapping
            results for their particular region. The GLIMS Glacier Database
            provides students, educators, scientists, and the public with
            reliable glacier data from these analyses. New glacier data are
            continually being added to the database."""
        ),
        'citation': {
            'text': (
                """GLIMS and NSIDC (2005, updated 2013): Global Land Ice
                Measurements from Space glacier database.  Compiled and made
                available by the international GLIMS community and the National
                Snow and Ice Data Center, Boulder CO, U.S.A.
                DOI:10.7265/N5V98602"""
            ),
            'url': 'https://doi.org/10.7265/N5V98602',
        },
    },
)
