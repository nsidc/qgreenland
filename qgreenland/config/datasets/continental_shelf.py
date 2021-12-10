from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


continental_shelf = Dataset(
    id='continental_shelf',
    assets=[
        HttpAsset(
            id='north_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_points.zip',
            ],
        ),
        HttpAsset(
            id='north_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_lines.zip',
            ],
        ),
        HttpAsset(
            id='north_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_76_2014_polygons.zip',
            ],
        ),
        HttpAsset(
            id='northeast_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_points.zip',
            ],
        ),
        HttpAsset(
            id='northeast_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_lines.zip',
            ],
        ),
        HttpAsset(
            id='northeast_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_68_2013_polygons.zip',
            ],
        ),
        HttpAsset(
            id='south_points',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_points.zip',
            ],
        ),
        HttpAsset(
            id='south_lines',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_lines.zip',
            ],
        ),
        HttpAsset(
            id='south_polygons',
            urls=[
                'http://tuvalu.grida.no/ecs/dnk_61_2012_polygons.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Denmark - in respect of the Continental Shelf of Greenland',
        'abstract': (
            """On 15 December 2014, the Kingdom of Denmark submitted to the
            Commission on the Limits of the Continental Shelf, in accordance with Article 76, paragraph 8,
            of the Convention, information on the limits of the continental shelf beyond 200 nautical miles
            from the baselines from which the breadth of its territorial sea is measured in respect of
            the Northern Continental Shelf of Greenland. It is noted that the Convention entered into force
            for Denmark on 16 December 2004. According to the submitting State, this is a “partial submission
            of the Government of the Kingdom of Denmark together with the Government of Greenland”.
            In accordance with the Rules of Procedure of the Commission (CLCS/40/Rev.1), a communication is being
            circulated to all Member States of the United Nations, as well as States Parties to the Convention,
            in order to make public the executive summary of the partial submission, including all charts and
            coordinates contained in that summary. The consideration of the submission made by Denmark will be
            included in the provisional agenda of the thirty-eighth session of the Commission to be held in
            New York from 20 July to 4 September 2015. Upon completion of the consideration of the submission,
            the Commission shall make recommendations pursuant to Article 76 of the Convention."""
        ),
        'citation': {
            'text': (
                """Kingdom of Denmark together with the Government of Greenland."""
            ),
            'url': 'http://continentalshelf.org/onestopdatashop/6350.aspx',
        },
    },
)
