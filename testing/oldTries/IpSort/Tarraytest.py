#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess


dName = sys.argv[1]

array = [['IP', 'SUB']]

ofName = dName + "IParray.txt"
outputFile = open(ofName, "w")

with open(dName + 'ipaddr.txt') as IPdom:
	for line in IPdom:
		line = line.rstrip('\n')
		var = line.split( '|' )
		array.append(var)


arrayall = [['IP', 'SUBS']]

arrayall[0].append(array[1][1])
arrayall[0].append(array[2][1])

arrayall[1].extend(array[4][1])
arrayall[1].extend(array[3][1])

print (arrayall)
