from qgreenland.config.layers.Glaciology.glacier_terminus_ import layers
from qgreenland.config.layers.Glaciology.glacier_terminus_ import LAYER_YEARS


ORDER_LAYERS = [
    id_str(START, END)
    for (START, END) in LAYER_YEARS
]


def id_str(*, START: int, END: int) -> str:
    return f'glacier_terminus_{START}_{END}'
