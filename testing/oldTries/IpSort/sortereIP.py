#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess

dName = sys.argv[1]

array = [['IP', 'SUB']]


with open(dName + 'ipaddr.txt') as IPdom:
	for line in IPdom:
		line = line.rstrip('\n')
		var = line.split( '|' )
		array.append(var)

outputFile = open(dName + 'usortereIP.txt', "w")

for i in array:
	ip = i.pop(0)
#	ip = ip.strip()
	for s in ip:
		outputFile.write(s+"\n")

outputFile.close()
IPdom.close()

