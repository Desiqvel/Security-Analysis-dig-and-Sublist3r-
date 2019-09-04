#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os

dName = sys.argv[1]

print ("Starting to print from " + dName)

subdomains = sublist3r.main(dName, 40, dName + '.sub.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)

#myCmd = ("dig -f %s.sub.txt +short > %s.ipaddr.txt" % (dName, dName))
#os.system(myCmd)

#del2

ofName = dName + ".IP_SUB.txt"
outputFile = open(ofName, "w")
iplist = dName + ".IPunsort.txt"
outputIP = open(iplist, "w")

with open(dName + '.sub.txt') as text_file:
        for domainName in text_file:
                domainName = domainName.rstrip()
                cmd = ("dig %s +short | grep -P '^(?:(?![a-z]).)*$'" % domainName)
                ip = os.popen(cmd).read()
                ip = ip.rstrip()
                ip = ip.split('\n')
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



#del 3

with open(dName + '.IPunsort.txt', "r") as infile:
	iplist = sorted([i.strip() for i in infile.readlines()], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))


with open(dName + ".unsIP.txt", "w") as outfile:
	outfile.write("\n".join(i for i in iplist))


# Check if the length is greater than zero
with open(dName + ".unsIP.txt", 'r') as inp, open(dName + '.sortedIP.txt', 'w') as out:
	for line in inp:
		if len(line.strip()) > 0:
			out.write(line)


infile.close()
outfile.close()
