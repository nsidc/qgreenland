from qgreenland.config.datasets.ice_iso_map import ice_iso_map as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


ice_iso_map = ConfigLayer(
    id='ice_iso_map',
    title='Ice Isopachs',
    description=(
        """Onshore ice isopachs for the landmass of Greenland"""
    ),
    tags=[],
    style='ice_isopachs',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *compressed_vector(
            input_file='{input_dir}/as_2159.zip',
            output_file='{output_dir}/final.gpkg',
            vector_filename='Greenland_ice/*.shp',
        ),
    ],
)

ice_isopachs = ConfigDataset(
    id='ice_iso_map',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_land.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Onshore ice isopachs for the landmass of Greenland',
        'abstract': (
            """This linear feature class contains onshore ice isopachs for the landmass of Greenland. 
            The isopochs illustrate the variation in ice thickness with a contour interval of 250 metres. 
            The data set was provided by the Geological Survey of Denmark and Greenland."""
        ),
        'citation': {
            text': (
                """Harrison, J.C., St-Onge, M.R., Petrov, O.V., Strelnikov,
                S.I., Lopatin, B.G., Wilson, F.H., Tella, S., Paul, D., Lynds,
                T., Shokalsky, S.P., Hults, C.K., Bergman, S., Jepsen, H.F., and
                Solli, A., 2011. Geological map of the Arctic / Carte gologique
                de l'Arctique; Geological Survey of Canada, Map 2159A, scale 1:5
                000 000."""
            ),
            'url': 'https://doi.org/10.4095/287868',
        },
    },
)
