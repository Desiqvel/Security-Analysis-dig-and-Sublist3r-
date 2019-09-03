#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess


array = [['IP', 'SUB']]


with open('nrk.noipaddr.txt') as IPdom:
	for line in IPdom:
		line = line.rstrip('\n')
		var = line.split( '|' )
		array.append(var)
i = 1
for i in array:
	ip = i.pop(0)
	ip = ip.strip()
	print(ip)

#ip.sort(key=lambda s: map(int, s.split('.')))

#from collections import namedtuple
#ip_type = namedtuple("IP", 'g1 g2 g3 g4 port')

#def to_ip(string) -> ip_type:
#    g1, g2, g3, g4 = [int(g) for g in string.split('.')]
#    return ip_type(g1, g2, g3, g4 )


#print(sorted(array, key=to_ip))

#print (ip)
outputFile = open('usortereIP.txt', "w")

for s in ip:
	outputFile.write(s+"\n")

#outputFile.close()
IPdom.close()

