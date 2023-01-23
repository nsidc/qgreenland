from qgreenland.config.datasets.caff import caff_char as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput

caff_char = Layer(
    id="caff_char",
    title="Arctic Char populations 2010",
    description=(
        """Polygons indicating the 2010 distribution of Arctic Char
        populations."""
    ),
    tags=[],
    style="semitransparent_polygon",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *compressed_vector(
            input_file="{input_dir}/Arctic_Char_2010.zip",
            output_file="{output_dir}/final.gpkg",
            ogr2ogr_args=(
                "-dialect",
                "sqlite",
                "-sql",
                (
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
