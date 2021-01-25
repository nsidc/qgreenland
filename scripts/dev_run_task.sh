#!/bin/bash

# Run the cleanup script if the user passes any arguments. Convenient to do
# everything in one step.
if [ -n "$1" ]; then
    echo "🧹Doing cleanup..."
    THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"
    $THIS_DIR/cleanup.sh $@
    echo "🧹Cleanup done!"
fi


# Skip zipping the package because in dev we typically want to examine
# the results.
docker-compose exec ${tty_arg} luigi luigi --workers=1 \
  --module qgreenland.tasks.main CreateQgisProjectFile
