#!/bin/bash
# NOTE: the short name is part of ganule_ur: SC:RDBTS4.001:114194114
#                                               ^^^^^^
set -e

if [ -z "$1" ]; then
   echo "Expected collection short name as first argument!"
   exit 1
fi

SHORT_NAME="$1"
URL="https://graphql.earthdata.nasa.gov/api"

QUERY="{collections (shortName: \\\"$SHORT_NAME\\\") {items {conceptId, shortName, versionId}}}"

echo "$QUERY"

curl -XPOST -H "Content-Type: application/json" \
     --data "{\"query\": \"$QUERY\"}" \
     "$URL"
