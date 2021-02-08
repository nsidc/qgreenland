#!/bin/bash
set -e

REPO_ROOT='http://ramadda.science.uu.nl:8080/repository/entry/get/WCE%20RAMADDA%20Data%20Repository/data/tmp/brice/Stafford'
DEST_ROOT='/share/appdata/qgreenland-private-archive/racmo_qgreenland_jan2021'

if [[ -z "$USERNAME" || -z "$PASSWORD" ]]; then
    echo "Please populate \$USERNAME and \$PASSWORD envvars."
    exit 1
fi

# 5.5km
wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/wind/5.5km-EPSG3413/v10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km_EPSG3413.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/wind/5.5km-EPSG3413/u10m.1958-2019.BN_RACMO2.3p2_FGRN055_5.5km_EPSG3413.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

# 1km
wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/t2m.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/subl.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/snowmelt.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/snowfall.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/sndiv.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/smb_rec.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/runoff.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/refreeze.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT

wget --user "$USERNAME" --password "$PASSWORD" \
    $REPO_ROOT/1km/mean/precip.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc.gz --directory-prefix=$DEST_ROOT
