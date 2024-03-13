#!/bin/sh

docker rm $1 -f
docker system prune -a

docker build . -t $1
docker run --name $1 -p 1337:1337 --platform linux/amd64 --privileged $1 