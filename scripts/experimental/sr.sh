#/usr/bin/env bash
# NOTE: This is meant to run with GNU `sed`. Use homebrew (OSX) to get GNU
# `sed` or run this script inside a linux container if you're not a Linux user.

SEARCH="$1"; shift
REPLACE="$1"; shift

if [[ -z ${SEARCH} || -z ${REPLACE} ]]; then
    echo "Two positional arguments expected: SEARCH and REPLACE."
    exit 1
fi

grep --color -R --include="*.py" ${SEARCH} *
echo "WARNING: Replacing \"${SEARCH}\" with \"${REPLACE}\" in the files listed above."
read -rp "Press ENTER to continue, CTRL+C to cancel."
echo ""

grep -rl "${SEARCH}" --include="*.py" | \
    xargs -d '\n' sed -i -e "s/${SEARCH}/${REPLACE}/g"
