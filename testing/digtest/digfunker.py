#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess

dName = sys.argv[1]

ofName = dName + "output.txt"
outputFile = open(ofName, "w")
iplist = dName + "IPout.txt"
outputIP = open(iplist, "w")

with open(dName + 'sub.txt') as text_file:
	for domainName in text_file:
		domainName = domainName.rstrip()
		cmd = ("dig %s +short | grep -P '^(?:(?![a-z]).)*$'" % domainName)
		ip = os.popen(cmd).read()
		ip = ip.rstrip()
		ip = ip.split('\n')
  #     	 outputFile.write("Domain:>"+domainName+", IP:>"+ip+"<")
		if len(ip) > 1:
			for line in ip:
				outputFile.write(line+"|"+domainName+"\n")
		else:
			outputFile.write(ip[0]+"|"+domainName+"\n")
	#planen her er å legge den i en array og sjekke om den allerede finnes
	#i arrayen, hvis ikke legger man den inn, deretter skriver til en fil.
		outputIP.write(ip[0]+"\n")


outputFile.close()
outputIP.close()
text_file.close()
