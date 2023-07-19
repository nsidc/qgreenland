from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

layers = [
    Layer(
        id=layer_id,
        title=layer_id.capitalize(),
        style="labeled_point",
        description=f"Points representing {layer_id} in Greenland.",
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
    for layer_id in ("cities", "settlements")
]
