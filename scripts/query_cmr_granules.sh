#!/bin/bash
set -e

python -c "from qgreenland.util.cmr import pretty_search_cmr_granules; pretty_search_cmr_granules(short_name='$1', version='$2')"
