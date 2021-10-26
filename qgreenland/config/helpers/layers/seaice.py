import calendar


def layer_title(month: int) -> str:
    return calendar.month_name[month]


def layer_id(month: int) -> str:
    return f'seaice_median_extent_{month:02d}'
