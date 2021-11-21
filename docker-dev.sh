#!/bin/bash 

source colors.sh

echo "........ docker compose ......."
command=$(docker-compose -f docker-compose.dev.yml build)
if [ $? -eq 0 ]; then
    echo
    echo docker-compose docker-compose.dev.yml build $(green OK)
    echo
else
    echo docker-compose.dev.yml build $(red  Failed)
fi

command=$(docker rm -f cms-cont)
command=$(docker volume rm $(docker volume ls))
command=$(docker-compose -f docker-compose.dev.yml up)
