from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

gshhg_coastlines = Dataset(
    id="gshhg_coastlines",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "http://www.soest.hawaii.edu/pwessel/gshhg/gshhg-shp-2.3.7.zip",
            ],
        ),
    ],
    metadata={
        "title": (
            "GSHHG: A Global Self-consistent, Hierarchical, High-resolution"
            " Geography Database"
        ),
        "abstract": (
            """We present a high-resolution geography data set amalgamated from
            three data bases in the public domain:

                World Vector Shorelines (WVS).
                CIA World Data Bank II (WDBII).
                Atlas of the Cryosphere (AC).

            The WVS is our basis for shorelines except for Antarctica while the
            WDBII is the basis for lakes, although there are instances where
            differences in coastline representations necessitated adding WDBII
            islands to GSHHG. The WDBII source also provides all political
            borders and rivers. The addition of AC since 2.3.0 allows us to
            offer two choices for Antarctica coastlines: Ice-front or Grounding
            line. These are encoded as levels 5 and 6, respectively and users of
            GSHHG can choose which set to use. GSHHG data have undergone
            extensive processing and should be free of internal inconsistencies
            such as erratic points and crossing segments. The shorelines are
            constructed entirely from hierarchically arranged closed polygons. A
            modified version of GSHHG is used by GMT, the Generic Mapping Tools.
            Starting with version 2.2.2, GSHHG has been released under the GNU
            Lesser General Public License."""
        ),
        "citation": {
            "text": (
                """Wessel, P., and W. H. F. Smith, A Global Self-consistent,
                Hierarchical, High-resolution Shoreline Database, J. Geophys.
                Res., 101, 8741-8743, 1996"""
            ),
            "url": (
                "https://www.soest.hawaii.edu/pwessel/gshhg/"
                "Wessel+Smith_1996_JGR.pdf"
            ),
        },
    },
)
