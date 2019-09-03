#!/usr/bin/env python3

import ipaddress
import sublist3r
import sys
import os
import subprocess

dName = "nrk.noIPout.txt"


with open(dName, "r") as infile:
	iplist = sorted([i.strip() for i in infile.readlines()], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))


with open("NYsortedip.txt", "w") as outfile:
	outfile.write("\n".join(i for i in iplist))


# Check if the length is greater than zero
with open("NYsortedip.txt", 'r') as inp, open('plz.txt', 'w') as out:
	for line in inp:
		if len(line.strip()) > 0:
			out.write(line)


infile.close()
outfile.close()

