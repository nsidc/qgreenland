START = 2005
END = 2017

LAYER_YEARS = [
    (2000, 2001),
    *[
        (START, START + 1)
        for year in range(2005, 2017 + 1)
    ],
]


def id_str(*, start: int, end: int) -> str:
    return f'glacier_terminus_{start}_{end}'


LAYER_IDS = [
    id_str(start=START, end=END)
    for (START, END) in LAYER_YEARS
]
