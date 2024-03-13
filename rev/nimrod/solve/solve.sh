echo "MAKE SURE TO REPLACE THE uin1 AND uin2 VALUES IN sol.py"
echo "DID YOU REPLACE? (y/n)"
read choice
if [[ $choice != *"y"* ]]; then
    docker run -d --platform=linux/amd64 --name nimrod-pcap menoone/nimrod
    docker cp nimrod-pcap:/root/network.pcap .
    docker rm -f nimrod-pcap
    echo "THEN GO CHANGE"
    echo "FILE COPIED IN THIS DIRECTORY"
    exit
fi

docker rm -f nimrod-solver
docker rmi nimrod-solver
docker build -t nimrod-solver .
docker run -d --platform=linux/amd64 --name nimrod-solver nimrod-solver

docker exec -u n00b -w /tmp nimrod-solver bash -c "python3 sol.py"
docker exec -u n00b -w /home/n00b nimrod-solver bash -c "grep -r pearl ."

docker rm -f nimrod-solver
docker rmi nimrod-solver
