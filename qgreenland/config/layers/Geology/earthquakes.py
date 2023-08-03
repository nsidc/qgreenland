from qgreenland.config.datasets.earthquakes import earthquakes as dataset
from qgreenland.config.datasets.geus import geus_cryo_seismic_events
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

earthquakes = Layer(
    id="earthquakes",
    title="Earthquakes M above 2.5 1900-2022",
    description=("""Location and magnitude of earthquakes."""),
    tags=[],
    style="earthquakes",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        CommandStep(
            args=[
                "ogrmerge.py",
                "-single",
                "-o",
                "{output_dir}/earthquakes.gpkg",
                "{input_dir}/*geojson",
            ],
        ),
        *ogr2ogr(
            input_file="{input_dir}/earthquakes.gpkg",
            output_file="{output_dir}/earthquakes.gpkg",
            boundary_filepath=project.boundaries["background"].filepath,
            ogr2ogr_args=(
                "-dialect",
                "sqlite",
                "-sql",
                """\"SELECT
                    geom,
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
                FROM merged\"""",
            ),
        ),
    ],
)

cryo_seismic_events = Layer(
    id="cryo_seismic_events",
    title="Cryo-generated seismic events",
    description=(
        """Cryo-generated seismic events.

The datetime of each event is given in UTC. For additional data on each event,
see
https://dataverse.geus.dk/dataset.xhtml?persistentId=doi:10.22008/FK2/ABMBLO"""
    ),
    tags=[],
    # TODO:
    style=None,
    input=LayerInput(
        dataset=geus_cryo_seismic_events,
        asset=geus_cryo_seismic_events.assets["only"],
    ),
    steps=[
        CommandStep(
            id="create_source",
            args=[
                'echo "datetime; lat; lon" > {output_dir}/cryo_with_header.csv',
                "&&",
                "cat {input_dir}/cryo.lis >> {output_dir}/cryo_with_header.csv",
            ],
        ),
        *ogr2ogr(
            input_file="{input_dir}/cryo_with_header.csv",
            output_file="{output_dir}/cryo_events.gpkg",
            boundary_filepath=project.boundaries["background"].filepath,
            ogr2ogr_args=(
                "-s_srs",
                "EPSG:4326",
                "-oo",
                "X_POSSIBLE_NAMES=lon",
                "-oo",
                "Y_POSSIBLE_NAMES=lat",
            ),
        ),
        *ogr2ogr(
            input_file="{input_dir}/cryo_events.gpkg",
            output_file="{output_dir}/cryo_events_with_datetime.gpkg",
            boundary_filepath=project.boundaries["background"].filepath,
            ogr2ogr_args=(
                "-dialect",
                "sqlite",
                "-sql",
                """\"SELECT
                geom,
                substr(datetime, 1, 4) || '-' || substr(datetime, 6, 2) || '-' || substr(datetime, 8, 2) || 'T' || substr(datetime, 11, 2) || ':' || substr(datetime, 13, 2) as datetime
                FROM cryo_with_header\"""",
            ),
        ),
    ],
)
