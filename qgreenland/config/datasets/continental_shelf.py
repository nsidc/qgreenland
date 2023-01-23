from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

continental_shelf = Dataset(
    id="continental_shelf",
    assets=[
        HttpAsset(
            id="north_points",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_76_2014_points.zip",
            ],
        ),
        HttpAsset(
            id="north_lines",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_76_2014_lines.zip",
            ],
        ),
        HttpAsset(
            id="north_polygons",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_76_2014_polygons.zip",
            ],
        ),
        HttpAsset(
            id="northeast_points",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_68_2013_points.zip",
            ],
        ),
        HttpAsset(
            id="northeast_lines",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_68_2013_lines.zip",
            ],
        ),
        HttpAsset(
            id="northeast_polygons",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip",
            ],
        ),
        HttpAsset(
            id="south_points",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip",
            ],
        ),
        HttpAsset(
            id="south_lines",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_61_2012_lines.zip",
            ],
        ),
        HttpAsset(
            id="south_polygons",
            urls=[
                "http://tuvalu.grida.no/ecs/dnk_61_2012_polygons.zip",
            ],
        ),
    ],
    metadata={
        "title": "Continental Shelf Programme",
        "abstract": (
            """The Kingdom of Denmark's submission to the Commission on the Limits of the Continental
            Shelf. This is in accordance with Article 76, paragraph 8 of the United Nations Convention
            on the Law of the Sea of 10 December 1982, which represents information on the limits of the
            continental shelf beyond 200 nautical miles from the baselines from which the breadth of its
            territorial sea is measured in respect of the Continental Shelf of Greenland."""
        ),
        "citation": {
            "text": (
                """Continental Shelf Programme. Denmark - in respect of the continental shelf
                of Greenland. 2012-2015. GRID-Arendal. Retrieved December 2021
                (http://www.continentalshelf.org/onestopdatashop/6350.aspx). """
            ),
            "url": "http://continentalshelf.org/onestopdatashop/6350.aspx",
        },
    },
)
