repo="flensing"
flag="YOUREALLYTHOUGHTTHATGRABBINGFILESANDREVERSINGWOULDWORK?FIXTHEIMAGEANDRUNME"

docker images | grep ${repo}

echo "Overwrite image (if exists) (y/N)"
read choice

case $choice in
    "Y")
        echo "[+] overwriting pre-existing image"
    ;;
    "y")
        echo "[+] overwriting pre-existing image"
    ;;
    *)
        echo "[+] Abort request recieved! Stopping build"
        exit
esac

# build and commit init image
docker build -t flensing-init .
docker rm -f flensing-init

docker run -d --name flensing-init flensing-init

docker exec flensing-init pip install pycryptodome
docker exec -e FLAG=$flag flensing-init /app/runme.py
docker exec flensing-init ash -c "echo 'import base64' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"
docker exec flensing-init ash -c "echo 'srand = [149, 148, 136, 91, 178, 110, 125, 77, 66, 155, 72, 225, 29, 218, 254, 208, 87, 113, 183, 123, 97, 193, 182, 216, 146, 142, 18, 211]' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"
docker exec flensing-init ash -c "echo 'urand = [246, 211, 222, 51, 209, 3, 5, 122, 32, 241, 10, 135, 127, 176, 179, 170, 13, 55, 142, 75, 44, 135, 143, 179, 223, 223, 47, 238]' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"
docker exec flensing-init ash -c "echo 'prand = [118, 51, 95, 102, 48, 114, 95, 52, 109, 98, 51, 114, 103, 49, 115, 125]' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"
docker exec flensing-init ash -c "echo 'print(base64.b64decode(str().join(chr(urand[i] ^ srand[i]) for i in range(len(urand))).encode()).decode())' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"
docker exec flensing-init ash -c "echo 'exit()' >> /usr/local/lib/python3.12/site-packages/Crypto/__init__.py"

docker commit flensing-init flensing-secret

# build and commit secret image
docker run -d --name flensing-secret flensing-secret
docker exec flensing-secret rm /root/secret
docker commit flensing-secret flensing-status

# build and commit status image
docker run -d --name flensing-status flensing-status
docker exec flensing-status rm /var/log/status
docker commit flensing-status $repo

# generate tar ball from image
docker save flensing -o flensing-original.tar

# clean up 
docker rm -f flensing-init flensing-secret flensing-status
docker rmi flensing-init flensing-secret flensing-status

echo "I am done now"
echo "Go on edit manually LOL"