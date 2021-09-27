#!/bin/bash
THIS_DIR="$( readlink -f "$( dirname "${BASH_SOURCE[0]}" )")"

"$THIS_DIR"/container_cli.sh cleanup "$@"
