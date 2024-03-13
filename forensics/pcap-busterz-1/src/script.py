from PIL import Image
import socket
import time
import random

path = "./qrcode.png"


img = Image.open(path)

pixel_data = img.load()

host = '172.31.122.157'
port = 1234

data=[]

for x in range(100):
	for y in range(100):
		color = "white"
		if(pixel_data[x,y] == (0,0,0,255)):
			color = "black"

		data.append(f"x={x}, y={y}, color={color}")

random.shuffle(data)
i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host, port))

	for line in data:
		s.sendall(line.encode() + b'\n')
		print(i)
		i+=1
		time.sleep(0.001)