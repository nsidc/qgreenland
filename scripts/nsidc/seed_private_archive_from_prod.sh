#!/bin/bash
set -e

LOCAL_PRIVATE_ARCHIVE_DIR='/share/appdata/qgreenland-private-archive/'
PROD_PRIVATE_ARCHIVE_DIR='/share/appdata/qgreenland-private-archive/'
PROD_HOSTNAME='qgreenland.apps.int.nsidc.org'
VAGRANT_SSH_KEY="$HOME/.ssh/id_rsa_vagrant_vsphere"

if [ ! -w ${LOCAL_PRIVATE_ARCHIVE_DIR} ]; then
    echo "${LOCAL_PRIVATE_ARCHIVE_DIR} must be writable to continue."
    exit 1
fi

rsync -a --progress --verbose \
    -e "ssh -i ${VAGRANT_SSH_KEY}" \
    vagrant@${PROD_HOSTNAME}:${PROD_PRIVATE_ARCHIVE_DIR} ${LOCAL_PRIVATE_ARCHIVE_DIR}
