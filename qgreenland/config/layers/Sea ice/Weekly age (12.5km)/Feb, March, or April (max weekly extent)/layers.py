from qgreenland.config.helpers.layers.sea_ice_age import create_sea_ice_age_layers

# TODO: this is weekly data, so does it really belong in a group called
# 'Feb or March'?

seaice_minimum_age_layers = create_sea_ice_age_layers("maximum")
