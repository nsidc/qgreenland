#!/bin/bash
set -e

LOCAL_CACHE_DIR='/share/appdata/qgreenland-input-cache'
PROD_CACHE_DIR='/share/appdata/qgreenland-input-cache'
PROD_HOSTNAME='qgreenland.apps.int.nsidc.org'
VAGRANT_SSH_KEY="$HOME/.ssh/id_rsa_vagrant_vsphere"

if [ ! -w ${LOCAL_CACHE_DIR} ]; then
    echo "${LOCAL_CACHE_DIR} must be writable to continue."
    exit 1
fi

# In case of permission problems:
# sudo chown -R $USER:$USER $LOCAL_CACHE_DIR/*

rsync -a --progress --verbose \
    -e "ssh -i ${VAGRANT_SSH_KEY}" \
    vagrant@${PROD_HOSTNAME}:${PROD_CACHE_DIR}/* ${LOCAL_CACHE_DIR}/.
