#! /bin/bash python3

import os

def reqgen(dir):
	files = os.listdir(dir)
	
	if dir == "assets":
		dir = "./"
		os.chdir("assets")

	for file in files:
		if os.path.isdir(dir+file):
			reqgen(dir+file+"/")
		else:
			print("\tcase (\""+dir+file+"\"): return require(\""+dir+file+"\");")

print("switch(name) {")
reqgen("assets")
print("}")
