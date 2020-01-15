#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy

dName = sys.argv[1]

#lines_seen = set() # holds lines already seen
arraymerge = []
outfilemerge = open(dName + '.merged.txt', "w")
#with open(dName + '.sortNoDupIP.txt', "r") as sortip:

f = open(dName + '.sortNoDupIP.txt', 'r+')
lines = [i.strip() for i in f.readlines()]
for line in lines:
	arraymerge.append([line])
	for suborg in open(dName + '.IP_SUB.txt', "r"):
		sub = suborg.rstrip()
		sub = sub.split('|')
		temp = sub[1]
		print (temp)
		if line == sub[0]:
			if len(sub) > 1:
				outfilemerge.write(line +'|'+(for subline in sub: )




#arraymerge[line] = 
			arraymerge.append([line][temp])
#				if line not in lines_seen: 
	outfilemerge.write(arraymerge[line])
					#lines_seen.add(line)
	#arraymerge.append()
outfilemerge.close()


