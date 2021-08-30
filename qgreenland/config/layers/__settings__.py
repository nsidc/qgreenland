from qgreenland.models.config.layer_group import RootGroupSettings


# NOTE: Only "order" can be defined in the root group. Create a
# RootGroupSettings model for this?
settings = RootGroupSettings(
    order=[
        'Terrain Models',
        'Internet-required data',
        'Basemaps',
    ],
)
