#!/bin/sh
docker rm -f  runme
docker rmi runme

docker build --no-cache -t  runme .
docker run -p 30015:30015 --privileged --name runme runme

# docker exec -it contexto sh
