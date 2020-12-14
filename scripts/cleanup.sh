docker-compose up -d
docker-compose exec luigi ./tasks/qgreenland/qgreenland/util/cleanup.py $@
docker-compose down
