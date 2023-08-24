from qgreenland.models.config.asset import CommandAsset
from qgreenland.models.config.dataset import Dataset

geus_mineral_occurrences = Dataset(
    id="geus_mineral_occurrences",
    assets=[
        CommandAsset(
            id="only",
            args=[
                "ogr2ogr",
                "{output_dir}/geus_mineral_occurrences.gpkg",
                '"https://data.geus.dk/geusmap/ows/32624.jsp?service=WFS&mapname=greenland_portal&request=GetCapabilities&version=1.0.0"',
                "mineral_occurrences_v3_external",
            ],
        ),
    ],
    metadata={
        "title": "Greenland mineral occurrences map (GMOM) ",
        "abstract": (
            """Dataset containing a summary of geological information for known
            mineral occurrences on Greenland. The information includes the
            location, size, mineral commodities, mineralisation type,
            exploration history and a geological description of the deposit. The
            data has been collected and compiled from fieldwork investigations
            conducted by geological surveys, academic researchers and mineral
            exploration companies."""
        ),
        "citation": {
            "text": (
                """Thorning, L., Christensen, L. A., Dawes, P. R., Garde, A. A.,
                Heijboer, T. C., Kalvig, P., Larsen, L. M., Larsen, U., Nielsen, T. F.,
                Rehnström, E. F., Thomassen, B., Thrane, K., Schjøth, F. & Secher, K., 2011, "Updating of Greenland
                Mineral Occurrences Map (GMOM) on the Web", GEUS GeoNetwork catalogue, Revision date: 2022-04-19.
                {{date_accessed}}"""
            ),
            "url": "https://data.geus.dk/geonetwork/srv/eng/catalog.search#/metadata/8884ead8-45fc-4d1a-ae67-325182cde646",
        },
    },
)
