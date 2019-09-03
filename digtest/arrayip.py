#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess

dName = "nrk.no"

array = [['IP', 'SUB']]

ofName = dName + "IParray.txt"
outputFile = open(ofName, "w")

with open(dName + 'ipaddr.txt') as IPdom:
	for line in IPdom:
		var = line.split( '|' )
		array.append(var)



print(array[4][1])

i = 0
k = 0
arrayall = [['IP', 'SUBS']]
while k < len(array):
	for i in array:
	
	i += 1

for i in array:
	ip = array[i][0]
	ipsub = array[i][1]
	for k in array:
		sub = array[k][1]
		if sub = ipsub:
			arrayremp = [sub]
			arrayall.append(
