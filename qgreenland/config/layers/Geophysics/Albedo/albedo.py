from qgreenland.config.datasets.albedo import (
    monthly_albedo as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.models.config.layer import Layer, LayerInput


layers = [Layer(
    id=f'albedo_{year}_07',
    title=f'July {year} albedo (1km)',
    description=(
        f"""Average broadband planar albedo for July {year} derived from
        the Ocean and Land Colour Instrument (OLCI) on board the European Union
        Copernicus Sentinel-3A satellite.

        Albedo is a fractional value ranging from 0-1 representing the amount of
        incident solar radiation reflected from the surface."""
    ),
    tags=[],
    style='albedo',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets[f'{year}_07'],
    ),
    steps=[
        *compress_and_add_overviews(
            input_file='{input_dir}/*.tif',
            output_file='{output_dir}/' + f'albedo_{year}_07.tif',
            dtype_is_float=True,
        ),
    ],
) for year in (2018, 2019)]
