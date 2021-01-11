# Skip zipping the package because in dev we typically want to examine
# the results.
docker-compose exec ${tty_arg} luigi luigi --workers=1 \
  --module qgreenland.tasks.main CreateQgisProjectFile
