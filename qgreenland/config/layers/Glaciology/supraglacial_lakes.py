from qgreenland.config.datasets.esa_cci import esa_cci_supraglacial_lakes as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

supraglacial_lakes = Layer(
    id="jakobshavn_supraglacial_lakes",
    title="Sermeq Kujalleq/Jakobshavn supraglacial lakes 2019",
    description=(
        """Supraglacial lake delineation on Sermeq Kujalleq/Jakobshavn for
        2019/05/01 and 2019/10/01 generated using Sentinel-2 satellite data."""
    ),
    tags=["water"],
    style="supraglacial_lakes",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        # TODO: *compressed_vector(...)??
        CommandStep(
            args=[
                "unzip",
                "{input_dir}/greenland_sgl_s2_20190501_20191001_jakobshavn_v1_1.zip",
                '"*merged*"',
                "-d",
                "{output_dir}",
            ],
        ),
        *ogr2ogr(
            input_file="{input_dir}/greenland_sgl_s2_20190501_20191001_jakobshavn_merged_v1_1.shp",
            output_file="{output_dir}/selected.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
            ogr2ogr_args=(
                "-dialect",
                "sqlite",
                "-sql",
                """\"SELECT
                    Geometry,
                    id1,
                    DATE(
                      substr(date, 1, 4)
                      || '-'
                      || substr(date, 5, 2)
                      || '-'
                      || substr(date, 7, 2)
                    ) as date,
                    area1,
                    elev,
                    source,
                    tile,
                    row
                FROM greenland_sgl_s2_20190501_20191001_jakobshavn_merged_v1_1\" """,
            ),
        ),
    ],
)
