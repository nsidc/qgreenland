from qgreenland.config.datasets.caff import caff_char as dataset
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


caff_char = ConfigLayer(
    id='caff_char',
    title='Arctic Char populations 2010',
    description=(
        """Polygons indicating the 2010 distribution of Arctic Char
        populations."""
    ),
    tags=[],
    style='semitransparent_polygon',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/Arctic_Char_2010.zip',
            output_file='{output_dir}/final.gpkg',
            ogr2ogr_args=(
                '-dialect', 'sqlite',
                '-sql', (
                    """'SELECT
                        Geometry,
                        SPECIES,
                        INTRODUCED,
                        OWNER,
                        DATA_URL,
                        SOURCE,
                        CREATED,
                        DATE(substr(MODIFIED, 7, 4) || "-" ||
                          substr(MODIFIED, 4, 2) || "-" ||
                          substr(MODIFIED, 1, 2)) as MODIFIED,
                        CONTACT
                    FROM Arctic_Char_2010'"""
                ),
            ),
        ),
    ],
)
