YEARS = [
    2000,
    *list(range(2005, 2007 + 1)),
    2012,
    *list(range(2014, 2016 + 1))
]

LAYER_YEARS = [(year, year + 1) for year in YEARS]


def id_str(*, start: int, end: int) -> str:
    return f'glacier_terminus_{start}_{end}'


LAYER_IDS = [
    id_str(start=START, end=END)
    for (START, END) in LAYER_YEARS
]
