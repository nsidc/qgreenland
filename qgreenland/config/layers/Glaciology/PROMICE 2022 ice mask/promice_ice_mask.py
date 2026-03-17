from qgreenland.config.datasets.promice_ice_mask import dataset as dataset
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

icemask_nunatak_polygon_layer = Layer(
    id="06_promice_2022_icemask_nunatak_polygon",
    title="Ice mask polygon",
    description=(
        """Outline of the Greenland Ice Sheet from August 2022 with the nunataks
        in its interior cut out, provided as a polygon vector feature."""
    ),
    tags=[],
    in_package=True,
    style="ice_mask_polygon",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["06_promice_2022_icemask_nunatak_polygon"],
        )
    ],
    steps=[],
)


icemask_raster_150_layer = Layer(
    id="13_promice_2022_icemask_raster_150m_v3",
    title="Ice mask raster (150m)",
    description=(
        """Raster ice mask (150m resolution) aligned with BedMachine (Morlighem 2017)."""
    ),
    tags=[],
    in_package=True,
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["13_promice_2022_icemask_raster_150m_v3"],
        )
    ],
    steps=[
        CommandStep(
            args=[
                "gdalwarp",
                "-co",
                "COMPRESS=DEFLATE",
                "{input_dir}/*.gpkg",
                "{output_dir}/converted_and_compressed.tif",
            ],
        )
    ],
)
