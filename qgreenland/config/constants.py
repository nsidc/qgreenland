"""WARNING: Do not import these constants from outside the config subpackage.

This will likely (immediately or eventually) result in an import cycle.
"""

# TODO: is this really what we want? Maybe we can load some constants from yaml?
# Maybe all of the project config should be yaml?
PROJECT_CRS = 'EPSG:3413'