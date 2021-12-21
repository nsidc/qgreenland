#!/usr/bin/env bash
# We have to do some extra post-processing because of our situation using
# temporary storage.
set -e

SRC=/qgreenland-tmp/working-storage
DST=/share/appdata/qgreenland/working-storage

# Copy data from the temporary location to the NFS where we get monitoring and
# backups.
rsync --rsync-path="sudo rsync" -avz \
    "${SRC}/release-layers/" "${DST}/release-layers"
rsync --rsync-path="sudo rsync" -avz \
    "${SRC}/release-packages/" "${DST}/release-packages"

# Clean up everything on the temp storage location except the fetch directory
./script/cleanup.sh -RL -RP -WP -WL
