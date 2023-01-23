from itertools import product


def depth_str(depth: int) -> str:
    if depth == 0:
        return "Surface"
    else:
        return f"{depth}m"


def id_str(*, depth: int, season: str) -> str:
    return f"woa2018_{depth}m_temperature_{season}"


SEASONS_FNS: dict[str, str] = {
    "winter": "woa18_decav_t13_04.nc",
    "summer": "woa18_decav_t15_04.nc",
}
DEPTHS_BANDS: dict[int, int] = {
    0: 1,
    50: 11,
    200: 25,
    500: 37,
}

# Sort by season first, then by depth
COMBINATIONS = list(product(SEASONS_FNS.keys(), DEPTHS_BANDS.keys()))
COMBINATIONS.sort(key=lambda x: x[0], reverse=True)
COMBINATIONS.sort(key=lambda x: x[1])

WOA2018_LAYER_ORDER = [
    id_str(depth=depth, season=season) for (season, depth) in COMBINATIONS
]
