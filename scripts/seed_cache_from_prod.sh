#!/bin/bash

LOCAL_CACHE_DIR='/share/appdata/qgreenland-input-cache/'
PROD_CACHE_DIR='/share/appdata/qgreenland-input-cache/'
PROD_HOSTNAME='qgreenland.apps.int.nsidc.org'
VAGRANT_SSH_KEY='~/.ssh/id_rsa_vagrant_vsphere'

if [ ! -w ${LOCAL_CACHE_DIR} ]; then
    echo "${LOCAL_CACHE_DIR} must be writable to continue."
    exit 1
fi

rsync -a --progress \
    -e 'ssh -i ${HOME}/.ssh/id_rsa_vagrant_vsphere' \
    vagrant@${PROD_HOSTNAME}:${PROD_CACHE_DIR} ${LOCAL_CACHE_DIR}
