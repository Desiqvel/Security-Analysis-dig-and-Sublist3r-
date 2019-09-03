#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess


dName = "nrk.noipaddr.txt"

sortedIP = open('sortedIP.txt', "w")

with open(dName,"r") as f:
	ip_list = [ip.strip() for ip in f.readlines()]
	for ip in sorted(ip_list, key = lambda ip: ( int(ip.split(".")[0], int(ip.split(".")[1]), int(ip.split(".")[2]), int(ip.split(".")[3])))
		sortedIP.write(ip+'\n')

f.close()
sortedIP.close()
