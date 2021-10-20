START = 2005
END = 2017

LAYER_YEARS = [
    (2000, 2001),
    *[
        (START, START + 1)
        for year in range(2005, 2017 + 1)
    ],
]

LAYER_IDS = [
    id_str(START, END)
    for (START, END) in LAYER_YEARS
]


def id_str(*, START: int, END: int) -> str:
    return f'glacier_terminus_{START}_{END}'
