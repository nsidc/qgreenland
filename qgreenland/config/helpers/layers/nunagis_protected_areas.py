from qgreenland.config.datasets.nunagis_protected_areas import nunagis_protected_areas
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput


_nunagis_protected_areas_params = {
    'nunagis_thickbilled_murre_colonies': {
        'title': 'Thickbilled Murre breeding colony 5km zones',
        'description': (
            """Polygons representing 5km zones protected for Thickbilled Murre
            breeding colonies."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Colonies of breeding Brünnichs guillemots%'",
        'group': 'Birds',
    },
    'nunagis_murre_group_1km_zones': {
        'title': 'Murre group 1km zones',
        'description': 'Polygons representing 1km zones protected for Muure groups.',
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Murre%'",
        'group': 'Birds',
    },
    'nunagis_seabirds_colonies': {
        'title': 'Seabird breeding colonies',
        'description': (
            """Polygons representing areas protected for seabird breeding
            colonies."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Colonies of breeding sea birds%'",
        'group': 'Birds',
    },
    'nunagis_bird_protected_areas': {
        'title': 'Bird protected areas',
        'description': 'Polygons representing areas protected for birds.',
        'style': 'nunagis_bird_protected_areas',
        'where_sql': (
            'type IN'
            "('Bird Protection Area', 'Important Bird Area of BirdLife International')"
        ),
        'group': 'Birds',
    },
    'nunagis_eider_protected_areas': {
        'title': 'Eider protected areas',
        'description': 'Polygons representing areas protected for Eiders.',
        'style': 'nunagis_eider_protected_areas',
        'where_sql': "type LIKE 'Eider%'",
        'group': 'Birds',
    },
    'nunagis_goose_protected_areas': {
        'title': 'Goose protected areas',
        'description': 'Polygons representing areas protected for geese.',
        'style': 'nunagis_goose_protected_areas',
        'where_sql': (
            "type IN ('Barnacle goose colony', 'Goose moulting and breeding areas')"
        ),
        'group': 'Birds',
    },
    'nunagis_unesco_treaty_zones': {
        'title': 'UNESCO treaty zones',
        'description': (
            """Polygons representing 5km zones protected for Thickbilled Murre
            breeding colonies."""
        ),
        'style': 'UNESCO_treaty_zones',
        'where_sql': "type IN ('UNESCO World Heritage Site', 'Ramsar area')",
        'group': 'Protected zones',
    },
    'nunagis_no_go_areas': {
        'title': 'No go areas',
        'description': (
            """Polygons representing areas that should not be entered."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'No Go Area'",
        'group': 'Protected zones',
    },
    'nunagis_closed_areas': {
        'title': 'Closed areas',
        'description': (
            """Polygons representing areas that are closed."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'Closed Area'",
        'group': 'Protected zones',
    },
    'nunagis_salt_or_saline_lake_100m_zones': {
        'title': 'Salt or saline lake 100m zones',
        'description': (
            """Polygons representing 100m zones protected for salt or saline
            lakes."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'Salt or saline lake 100m zone'",
        'group': 'Protected zones',
    },
    'nunagis_homothermic_spring_100m_zones': {
        'title': 'Homothermic spring 100m zones',
        'description': (
            """Polygons representing 100m zones protected for homothermic
            springs."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'Homothermic spring 100 m zone'",
        'group': 'Protected zones',
    },
    'nunagis_national_park': {
        'title': 'National park',
        'description': (
            """Polygon representing the area protected for the national park."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'National Park'",
        'group': 'Protected zones',
    },
    'nunagis_biological_important_areas': {
        'title': 'Biological important areas in the national park',
        'description': (
            """Polygons representing areas protected for biologically important
            areas in the national park."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'Biological Important Areas in the National Park'",
        'group': 'Protected zones',
    },
    'nunagis_nature_protection_areas': {
        'title': 'Nature protection areas',
        'description': (
            """Polygons representing areas protected for nature."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type = 'Nature Protection Area'",
        'group': 'Protected zones',
    },
}

BIRDS_LAYERS = [
    key
    for key, params in _nunagis_protected_areas_params.items()
    if params['group'] == 'Birds'
]
PROTECTED_ZONES_LAYERS = [
    key
    for key, params in _nunagis_protected_areas_params.items()
    if params['group'] == 'Protected zones'
]


def _make_layer(
    *,
    layer_id: str,
    title: str,
    description: str,
    style: str,
    where_sql: str,
) -> Layer:
    return Layer(
        id=layer_id,
        title=title,
        description=description,
        tags=[],
        style=style,
        input=LayerInput(
            dataset=nunagis_protected_areas,
            asset=nunagis_protected_areas.assets['only'],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/fetched.geojson',
                output_file='{output_dir}/' + f'{layer_id}.gpkg',
                ogr2ogr_args=[
                    '-dialect', 'sqlite',
                    '-sql',
                    f"""\"SELECT
                        DATETIME(
                          CAST(created_date AS INTEGER) / 1000, 'unixepoch'
                        ) as created_date,
                        DATETIME(
                          CAST(last_edited_date AS INTEGER) / 1000, 'unixepoch'
                        ) as last_edited_date,
                        *
                    FROM ESRIJSON
                    WHERE {where_sql}\" """,
                ],
            ),
        ],
    )


def make_layers(
    layer_ids: list[str],
) -> list[Layer]:
    return [
        _make_layer(
            layer_id=layer_id,
            title=params['title'],
            description=params['description'],
            style=params['style'],
            where_sql=params['where_sql'],
        )
        for layer_id, params in _nunagis_protected_areas_params.items()
        if layer_id in layer_ids
    ]
