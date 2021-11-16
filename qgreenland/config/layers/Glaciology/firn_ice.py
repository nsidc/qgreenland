from qgreenland.config.datasets.firn_ice_layer_thickness import (
    macferrin_etal_firn_ice_layer_thicknesses as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput


firn_ice_layer_thicknesses = Layer(
    id='firn_ice_layer_thicknesses',
    title='Ice slab thickness in firn ice 2010-2014',
    description=(
        """Ice slab thickness, in meters, in the top 20 meters of firn. Only
        slabs between 1 and 16 meters are included."""
    ),
    tags=[],
    style='firn_ice_points',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/Ice_Layer_Output_Thicknesses.gpkg',
            output_file='{output_dir}/final.gpkg',
            ogr2ogr_args=(
                '-sql', (
                    """'SELECT
                        geom,
                        fid,
                        Track_name,
                        CAST(Tracenumber AS INTEGER) as Tracenumber,
                        lat,
                        lon,
                        CAST(alongtrack_distance_m AS REAL) as alongtrack_distance_m,
                        CAST("20m_ice_content_m" AS REAL) as "20m_ice_content_m"
                    FROM Ice_Layer_Output_Thicknesses'"""
                ),
            ),
        ),
    ],
)
