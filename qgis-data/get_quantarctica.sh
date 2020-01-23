#!/bin/bash

set -ex

URL="data.pgc.umn.edu/gis/packages/quantarctica"
FILE="Quantarctica3.zip"

if [ ! -f "${FILE}" ]; then
  wget --show-progress "${URL}/${FILE}" --output-document "${FILE}"
fi

unzip -o "${FILE}"
