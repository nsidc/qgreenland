from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

layers = [
    Layer(
        id=layer_id,
        title=layer_id.capitalize(),
        style="labeled_point",
        description=params["description"],
        tags=["places"],
        input=LayerInput(
            dataset=asiaq_nunagis,
            asset=asiaq_nunagis.assets[layer_id],
        ),
        steps=[
            *ogr2ogr(
                input_file="{input_dir}/fetched.geojson",
                output_file="{output_dir}/final.gpkg",
                boundary_filepath=project.boundaries["data"].filepath,
                ogr2ogr_args=(
                    "-nln",
                    layer_id,
                    "-dialect",
                    "sqlite",
                    "-sql",
                    "\"SELECT geometry, Ny_grønlandsk as 'New Greenlandic', Ny_grønlandsk as 'label', Gammel_grønlandsk as 'Old Greenlandic', Dansk as Danish, Alternativt_stednavn  as 'Alternative placename', Indbyggertal_2016 as 'Population 2016' FROM ESRIJSON\"",
                ),
            ),
        ],
    )
    for layer_id, params in {
        "towns": {
            "description": (
                """Points representing towns/cities in Greenland.

QGreenland Team - Noted Data Issues:

* West coast of Greenland, near Paamiut: Ivittuut is abandoned."""
            ),
        },
        "settlements": {
            "description": (
                """Points representing settlements in Greenland.

QGreenland Team - Noted Data Issues:

* East Greenland: Ikkatteq is an abandoned airstrip and is not populated.

* Near Ittoqqortoormiit: Uunartoq is abandoned.

* Near Qaanaaq: Qeqertarsuaq and Moriusaq are abandoned.

* Near Upernavik: Tussaaq is abandoned.

* Near Uummannaq: Illorsuit and Nuugaatsiaq are two recently abandoned
  settlements (2017) due a massive landslide and subsequent tsunami."""
            ),
        },
    }.items()
]
