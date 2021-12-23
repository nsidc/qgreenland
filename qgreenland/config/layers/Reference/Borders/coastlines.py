from qgreenland.config.datasets.bas_coastlines import bas_coastlines
from qgreenland.config.datasets.gshhg import gshhg_coastlines
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


bas_greenland_coastlines = Layer(
    id='bas_greenland_coastlines',
    title='Greenland coastlines 2017',
    description=(
        """This layer should be used as the 'reference coastline' for
        Greenland."""
    ),
    tags=[],
    show=True,
    style='greenland_coastline',
    input=LayerInput(
        dataset=bas_coastlines,
        asset=bas_coastlines.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/Greenland_coast.zip',
            output_file='{output_dir}/greenland_coastline.gpkg',
        ),
    ],
)

global_coastlines = Layer(
    id='coastlines',
    title='Global coastlines',
    description=(
        """Note that the 'Greenland coastlines 2017' layer is preferred for
        Greenland."""
    ),
    tags=[],
    style='transparent_shape',
    input=LayerInput(
        dataset=gshhg_coastlines,
        asset=gshhg_coastlines.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/gshhg-shp-2.3.7.zip',
            output_file='{output_dir}/global_coastlines.gpkg',
            decompress_step_kwargs={
                'decompress_contents_mask': 'GSHHS_shp/f/GSHHS_f_L1.*',
            },
            vector_filename='GSHHS_shp/f/*.shp',
        ),
    ],
)
