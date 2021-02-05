#!/bin/bash

set -e

LOCAL_PRIVATE_ARCHIVE_DIR='/share/appdata/qgreenland-private-archive'
REMOTE_PRIVATE_ARCHIVE_DIR='/share/appdata/qgreenland-private-archive'
PROD_HOSTNAME="dev.qgreenland.$USER.dev.int.nsidc.org"
VAGRANT_SSH_KEY='~/.ssh/id_rsa_vagrant_vsphere'

if [ -z "$1" ]; then
    echo "Provide the id of a dataset to push to production."
    exit 1
fi


source_dir="${LOCAL_PRIVATE_ARCHIVE_DIR}/${1}/"
dest_dir="${REMOTE_PRIVATE_ARCHIVE_DIR}/${1}"

if [ ! -d "${source_dir}" ]; then
    echo "$source_dir does not exist."
    exit 1
fi

rsync -a --progress --verbose \
    -e "ssh -i ${HOME}/.ssh/id_rsa_vagrant_vsphere" \
    ${source_dir} vagrant@${PROD_HOSTNAME}:${dest_dir}
