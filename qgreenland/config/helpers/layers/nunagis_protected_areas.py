from qgreenland.config.datasets.nunagis_protected_areas import nunagis_protected_areas
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


_nunagis_protected_areas_params = {
    'nunagis_thickbilled_murre_colonies': {
        'title': 'Thickbilled Murre breeding colony 5km zones',
        'description': (
            """Polygons representing 5km zones protected for Thickbilled Murre
            breeding colonies."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Colonies of breeding Brünnichs guillemots%'",
    },
    'nunagis_murre_group_1km_zones': {
        'title': 'Murre group 1km zones',
        'description': 'Polygons representing 1km zones protected for Muure groups.',
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Murre%'",
    },
    'nunagis_seabirds_colonies': {
        'title': 'Seabird breeding colonies',
        'description': (
            """Polygons representing areas protected for seabird breeding
            colonies."""
        ),
        'style': 'protected_area_polygon',
        'where_sql': "type LIKE 'Colonies of breeding sea birds%'",
    },
    'nunagis_bird_protected_areas': {
        'title': 'Bird protected areas',
        'description': 'Polygons representing areas protected for birds.',
        'style': 'nunagis_bird_protected_areas',
        'where_sql': (
            'type IN'
            "('Bird Protection Area', 'Important Bird Area of BirdLife International')"
        ),
    },
    'nunagis_eider_protected_areas': {
        'title': 'Eider protected areas',
        'description': 'Polygons representing areas protected for Eiders.',
        'style': 'nunagis_eider_protected_areas',
        'where_sql': "type LIKE 'Eider%'",
    },
    'nunagis_goose_protected_areas': {
        'title': 'Goose protected areas',
        'description': 'Polygons representing areas protected for geese.',
        'style': 'nunagis_goose_protected_areas',
        'where_sql': (
            "type IN ('Barnacle goose colony', 'Goose moulting and breeding areas')"
        ),
    },
}


LAYER_IDS_ORDERED_LIST = list(_nunagis_protected_areas_params.keys())


def _make_layer(
    *,
    layer_id: str,
    title: str,
    description: str,
    style: str,
    where_sql: str,
) -> ConfigLayer:
    return ConfigLayer(
        id=layer_id,
        title=title,
        description=description,
        tags=[],
        style=style,
        input=ConfigLayerInput(
            dataset=nunagis_protected_areas,
            asset=nunagis_protected_areas.assets['only'],
        ),
        steps=[
            ConfigLayerCommandStep(
                args=[
                    'ogr2ogr',
                    *STANDARD_OGR2OGR_ARGS,
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
                    '{output_dir}/' + f'{layer_id}.gpkg',
                    '{input_dir}/fetched.geojson',
                ],
            ),
        ],
    )


def make_layers() -> list[ConfigLayer]:
    layers = []
    for layer_id, params in _nunagis_protected_areas_params.items():
        layers.append(
            _make_layer(
                layer_id=layer_id,
                title=params['title'],
                description=params['description'],
                style=params['style'],
                where_sql=params['where_sql'],
            ),
        )

    return layers
