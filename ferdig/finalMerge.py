#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os

dName = 'vg.no'

#lines_seen = set() # holds lines already seen
arraymerge = []
outfilemerge = open(dName + '.merged.txt', "w")
with open(dName + '.sortNoDupIP.txt', "r") as sortip:
	for line in sortip:
		arraymerge.append[line]
		for suborg in open(dName + '.IP_SUB.txt', "r"):
			sub = suborg.rstrip()
			sub = sub.split('|')
			temp = sub[1]
			if line = sub[0]:
				arraymerge[line] = arraymerge.extend([line][temp])
#					if line not in lines_seen: 
		outfilemerge.write(arraymerge[line])
					#lines_seen.add(line)
	#arraymerge.append()
outfilemerge.close()


