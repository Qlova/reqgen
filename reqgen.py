#! /bin/bash python3

import os
import pathlib
import sys

directory = "assets"

def reqgen(dir):
	files = os.listdir(dir)

	if dir == directory:
		dir = "./"
		os.chdir(directory)

	for file in files:
		if os.path.isdir(dir+file):
			reqgen(dir+file+"/")
		else:
			if pathlib.Path(file).suffix == ".png":
				print("\tcase (\""+dir+file+"\"): return require(\"./"+directory+"/"+dir+file+"\");")




if len(sys.argv) > 1:
	directory = sys.argv[1]

print("export function GetImage(name) {\nswitch(name) {")
reqgen(directory)
print("}\n}")
