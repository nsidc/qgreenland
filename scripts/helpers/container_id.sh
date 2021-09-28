#!/bin/bash

swarm_mode=$(docker info --format '{{.Swarm.LocalNodeState}}')

if [[ "$swarm_mode" == "active" ]]; then
    container_hash=$(docker service ps -f 'name=qgreenland_luigi.1' qgreenland_luigi -q --no-trunc | head -n1)
    if [ -z "$container_hash" ]; then
        echo "No running luigi (swarm) container found!"
        exit 1
    fi

    container_id="luigi.1.${container_hash}"
else
    container_hash=$(docker ps -q -f "name=luigi" --filter "status=running")
    if [ -z "$container_hash" ]; then
        echo "No running luigi container found!"
        exit 1
    fi
    container_id="luigi"
fi

echo "${container_id}"
