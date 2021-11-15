from qgreenland.config.datasets.tectonic_plates import tectonic_plates as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


FN_HASH = '339b0c56563c118307b1f4542703047f5f698fae'
FN = f'tectonicplates-{FN_HASH}'

tectonic_plate_boundaries = Layer(
    id='tectonic_plate_boundaries',
    title='Tectonic plate boundaries',
    description=(
        """Linestrings representing borders between tectonic plates."""
    ),
    tags=[],
    style='tectonic_plate_boundaries',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/' + f'{FN}.zip',
            output_file='{output_dir}/final.gpkg',
            boundary_filepath=project.boundaries['background'].filepath,
            decompress_step_kwargs={
                'decompress_contents_mask':
                    f'{FN}/PB2002_boundaries.*',
            },
            vector_filename=f'{FN}/*.shp',
        ),
    ],
)
