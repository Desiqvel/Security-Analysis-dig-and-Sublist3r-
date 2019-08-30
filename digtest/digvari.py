#!/usr/bin/env python3

import sublist3r 
#import dig
import sys
import os

dName = sys.argv[1]


#myfile = open(dName + 'ipaddr.txt', 'w')


#myCmd = ("dig -f %ssub.txt +short" % (dName))


with open(dName + 'sub.txt') as text_file: 
#open(dName + 'ipaddr.txt', 'w') as myfile:
	for line in text_file:
#			myfile.write(line)
#			myCmd = ("%s test  >> %sipaddr.txt" % (line))
			myCmd = ("%s >> %sipaddr.txt && dig %s +short | grep -P '^(?:(?![a-z]).)*$' >> %sipaddr.txt" % (line, dName, line, dName))
			os.system(myCmd)


#myfile.writelines(ipadr)
#		if IPv4Address(line) > 0:



#myfile.close()
text_file.close()
