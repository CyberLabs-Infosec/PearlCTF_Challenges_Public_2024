import pyshark
import json 
from math import fabs

cap=pyshark.FileCapture("D:\ctfdump/game.pcap")
points=[]

for c  in cap:
	try:
		if str(c["MINETEST.CLIENT"].command)=="0x0039":
			if str(c["MINETEST.CLIENT"].interact_action) in ["0","1","2"]:
				print(f"add block at x =",c["MINETEST.CLIENT"].interact_pointed_above_x," y = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show," z = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)
#place a block of brick so as to differentiate from surroundings
				points.append({"name":"wool:white","x":fabs(float(c["MINETEST.CLIENT"].interact_pointed_above_x)),"y":10*fabs(float(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)),"z":fabs(float(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show))})			
			elif str(c["MINETEST.CLIENT"].interact_action) in ["3"]:
				print(f"remove block at x =",c["MINETEST.CLIENT"].interact_pointed_above_x," y = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show," z = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)
#place a block of air to remove a block
				points.append({"name":"wool:white","x":float(c["MINETEST.CLIENT"].interact_pointed_above_x),"y":float(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show),"z":float(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)})			
	except:
		pass 



with open("pcap3.json","w") as outfile:
	json.dump(points,outfile)

	