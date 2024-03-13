import miney
import json

#connect to world
mt=miney.Minetest()

#load node coordinates to change
with open("pcap3.json","r") as infile:
	pts=json.load(infile)

mt.node.set(pts)

