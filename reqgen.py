#! /bin/bash python3

import os
import pathlib

def reqgen(dir):
	files = os.listdir(dir)

	if dir == "assets":
		dir = "./"
		os.chdir("assets")

	for file in files:
		if os.path.isdir(dir+file):
			reqgen(dir+file+"/")
		else:
			if pathlib.Path(file).suffix == ".png":
				print("\tcase (\""+dir+file+"\"): return require(\"./assets/"+dir+file+"\");")

print("export function GetImage(name) {\nswitch(name) {")
reqgen("assets")
print("}\n}")
