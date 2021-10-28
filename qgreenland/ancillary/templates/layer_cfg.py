# TODO: Cleanup all comments that aren't specific to your layer.
# TODO: Fill in and uncomment below:
# from qgreenland.config.datasets.{your_dataset_module} import (
#     {your_dataset_object} as dataset,
# )
# TODO: Consider using a helper to generate your layers from data patterns:
# from qgreenland.config.helpers.{your_helper_module} import (
#     {your_helper_function},
# )
# TODO: Uncomment below if needed:
# from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
# TODO: Uncomment below if needed:
# from qgreenland.models.config.step import ConfigLayerCommandStep


# The name of the `layer` variable doesn't matter here. You may create layers
# with a list comprehension as well, as long as you assign it to a variable.
layer = ConfigLayer(
    # TODO: Fill in `your_layer_id`:
    id='your_layer_id',
    # TODO: Fill in your layer title:
    title='Your layer title.',
    description=(
      # TODO: Fill in your layer description:
        """Your layer description."""
    ),
    # TODO: Fill in your layer tags:
    tags=['your', 'layer', 'tags'],
    # TODO: Uncomment and fill in `your_style` if needed:
    # style='your_style',
    input=ConfigLayerInput(
        dataset=dataset,
        # TODO: Fill in `your_asset_id`:
        asset=dataset.assets['your_asset_id'],
    ),
    steps=[
        # TODO: Your steps here. How should the layer be processed into the
        # correct projection, clipped to the correct boundary, etc.? You can
        # use a mix of helpers and explicit commands e.g.:
        #
        #     # Warp the data into the project projection and cut it to the
        #     # "data" boundary.
        #     *warp(
        #         input_file='{input_dir}/arcticdem_mosaic_100m_v3.0.tif',
        #         output_file='{output_dir}/arctic_dem.tif',
        #         cut_file=project.boundaries['data'].filepath,
        #     ),
        #     # Scale the data by multiple of 100, set the nodata value, and
        #     # change the data type to integer for improved compressibility.
        #     ConfigLayerCommandStep(
        #         args=[
        #             'gdal_calc.py',
        #             '--calc', '"A * 100.0"',
        #             '--NoDataValue', '-9999',
        #             '--type', 'Int32',
        #             '-A', '{input_dir}/arctic_dem.tif',
        #             '--outfile', '{output_dir}/arctic_dem_scaled.tif',
        #         ],
        #     ),
        #     # Add a scale attribute which allows the values scaled above to
        #     # be displayed with approximately original values.
        #     *gdal_edit(
        #         input_file='{input_dir}/arctic_dem_scaled.tif',
        #         output_file='{output_dir}/arctic_dem.tif',
        #         gdal_edit_args=[
        #             '-scale', '0.01',
        #         ],
        #     ),
        #     # Compress the data with a lossless compression algorithm.
        #     *compress_raster(
        #         input_file='{input_dir}/arctic_dem.tif',
        #         output_file='{output_dir}/arctic_dem.tif',
        #     ),
        #     # Add raster overviews (tile pyramids) to the data for better
        #     # performance when zooming/panning.
        #     *build_overviews(
        #         input_file='{input_dir}/arctic_dem.tif',
        #         output_file='{output_dir}/arctic_dem.tif',
        #     ),
    ],
)
