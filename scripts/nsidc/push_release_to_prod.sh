#!/bin/bash
set -e

LOCAL_RELEASE_DIR='/share/appdata/qgreenland/release/'
PROD_RELEASE_DIR='/share/appdata/qgreenland/release/'
PROD_HOSTNAME='qgreenland.apps.int.nsidc.org'
VAGRANT_SSH_KEY="$HOME/.ssh/id_rsa_vagrant_vsphere"

echo "WARNING: THIS WILL OVERWRITE PRODUCTION LAYERS WITH LOCAL LAYERS AND SYNC ALL OF YOUR RELEASES TO PRODUCTION."
read -rp "PRESS CTRL-C TO CANCEL. PRESS ENTER TO PUSH STRAIGHT TO PROD AND DESTROY EVERYTHING."

sudo rsync --archive --progress --verbose \
    -e "ssh -i ${VAGRANT_SSH_KEY}" \
    --rsync-path='sudo rsync' \
    ${LOCAL_RELEASE_DIR}/* vagrant@${PROD_HOSTNAME}:${PROD_RELEASE_DIR}/
