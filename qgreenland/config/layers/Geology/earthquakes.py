from qgreenland.config.datasets.earthquakes import earthquakes as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


earthquakes = ConfigLayer(
    id='earthquakes',
    title='Earthquakes M above 2.5 1900-2020',
    description=(
        """Location and magnitude of earthquakes."""
    ),
    tags=[],
    style='earthquakes',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/query.geojson',
            output_file='{output_dir}/earthquakes.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-dialect', 'sqlite',
                '-sql', """\"SELECT
                    geometry,
                    id,
                    mag,
                    place,
                    DATETIME(time / 1000, 'unixepoch') as time,
                    DATETIME(updated / 1000, 'unixepoch') as updated,
                    tz,
                    url,
                    detail,
                    felt,
                    cdi,
                    mmi,
                    alert,
                    tsunami,
                    sig,
                    net,
                    code,
                    ids,
                    sources,
                    types,
                    nst,
                    dmin,
                    rms,
                    gap,
                    magType,
                    type,
                    title,
                    title as label
                FROM query\"""",
            ),
        ),
    ],
)