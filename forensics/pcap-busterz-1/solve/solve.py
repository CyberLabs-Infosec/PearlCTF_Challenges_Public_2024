"""
A pcap file has been provided, and upon careful inspection, it has been determined to contain data in the form of coordinates: 'x=val, y=val, color=val'. We can utilize Scapy to separate this data and plot the image. Data packets can be distinguished from others using the source IP '10.0.2.15' and destination IP '172.31.122.157'. Additionally, one packet may contain more than one coordinate.

Using this script, we can generate the image, which is a QR code. Scanning this QR code reveals the flag

flag : 
prompt : I have intercepted a pcap file on the dark web between unknown agents. 
    	 Help me decrypt it and find out what they're upto!!
link to file : https://mega.nz/file/cvRHhYoR#DdKDx-vDiLJUHVv07LX2g2KigGqJLJMWqOtxO-xHON4
"""

from scapy.all import *
from PIL import Image

file = "./sus.pcap"
co_ord = []

def extract_data(packet):
	if packet[IP].src == '10.0.2.15' and packet[IP].dst == '172.31.122.157':
		if Raw in packet:
			payload = (str(packet[Raw].load)[2:-1]).split('\\n')
			for p in payload:
				if(len(p)): 
					tmp = str(p).split(',')
					co_ord.append([int(tmp[0][2:]), int(tmp[1][3:]), tmp[2][7:]])

packets = rdpcap(file)
for packet in packets:
	extract_data(packet)
ht = 100
wd = 100

print(len(co_ord))
img = Image.new("RGBA", (ht,wd), "white")
pixel_data = img.load()

for data in co_ord:
	if(data[2] == 'white'):
		pixel_data[data[0], data[1]] = (255,255,255,255)
	else:
		pixel_data[data[0], data[1]] = (0,0,0,255)
    
img.save("qr_formed.png")
