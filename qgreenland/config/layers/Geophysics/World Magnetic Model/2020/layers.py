from qgreenland.config.helpers.layers import wmm

blackout_zones_layer = wmm.make_boz_layer(year=2020)

other_layers = wmm.make_wmm_variable_layers_for_year(year=2020)
