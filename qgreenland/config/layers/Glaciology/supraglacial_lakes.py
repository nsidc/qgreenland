from qgreenland.config.datasets.esa_cci import (
    esa_cci_supraglacial_lakes as dataset,
)
# from qgreenland.config.helpers.steps.build_overviews import build_overviews
# from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.config.project import project
from qgreenland.models.config.step import ConfigLayerCommandStep

supraglacial_lakes = ConfigLayer(
    id='jakobshavn_supraglacial_lakes',
    title='Sermeq Kujalleq/Jakobshavn supraglacial lakes 2019',
    description=(
        """Supraglacial lake delineation on Sermeq Kujalleq/Jakobshavn for
        2019/05/01 and 2019/10/01 generated using Sentinel-2 satellite data."""
    ),
    tags=['water'],
    style='supraglacial_lakes',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        ConfigLayerCommandStep(
            args=[
                'unzip',
                '{input_dir}/greenland_sgl_s2_20190501_20191001_jakobshavn_v1_1.zip',
                '"*merged*"',
                '-d', '{output_dir}',
            ],
        ),
        ConfigLayerCommandStep(
            args=[
                'ogr2ogr',
                '-lco', 'ENCODING=UTF-8',
                '-t_srs', project.crs,
                '-clipdst', project.boundaries['data'].filepath,
                '-dialect', 'sqlite',
                '-sql',
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
                '{output_dir}/selected.gpkg',
                '{input_dir}/greenland_sgl_s2_20190501_20191001_jakobshavn_merged_v1_1.shp',
            ],
        ),
    ],
)
