from qgreenland.config.project import project


STANDARD_OGR2OGR_ARGS = [
    '-lco', 'ENCODING=UTF-8',
    '-t_srs', project.crs,
]

