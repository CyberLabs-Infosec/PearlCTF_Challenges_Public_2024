docker rm -f nimrod-server
docker rmi nimrod-server
docker build -t nimrod-server .
docker run -d --platform=linux/amd64 --name nimrod-server -p 80:80 nimrod-server