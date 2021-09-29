#!/bin/bash

THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
container_id="$("$THIS_DIR"/helpers/container_id.sh)"

# Run the cleanup script if the user passes any arguments. Convenient to do
# everything in one step.
if [ -n "$1" ]; then
    echo "🧹Doing cleanup..."
    "$THIS_DIR"/cleanup.sh "$@"
    echo "🧹Cleanup done!"
fi


# Skip zipping the package because in dev we typically want to examine
# the results.
docker exec -it "${container_id}" luigi --workers=1 \
  --module qgreenland.tasks.main CreateQgisProjectFile
