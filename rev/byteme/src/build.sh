cd build/

docker rm -f byteme
docker rmi byteme
docker build -t byteme .
docker run -d --platform=linux/amd64 --name byteme byteme

docker cp byteme:/app/__pycache__/byteme.cpython-313.pyc ../byteme.pyc
docker cp byteme:/app/__pycache__/byteme.cpython-313.pyc ../../publish/byteme.pyc

# cleanup
docker rm -f byteme
docker rmi byteme
