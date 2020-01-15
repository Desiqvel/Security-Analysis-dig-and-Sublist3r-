#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy

dName = sys.argv[1]

#arraymerge = []
#outfilemerge = open(dName + '.merged.txt', "w")   	# Writes final merge to this file

arraymerge = []
count = -1

with open(dName + '.sortNoDupIP.txt', "r") as sortip: 	# Opens sorted IP-addresses
	arraymerge.append([])
	count = count+1
	ipsub = open(dName + '.IP_SUB.txt', "r")	# Opens IP-addresses with sub-domains
	for ip_sub in ipsub:				# Goes in a loop with all sub-domains
#		ip_sub = ipsub.rstrip()			# Strips whitespace Right
		ip_sub = ip_sub.split('|')		# Splits IP_SUB in IP-addresses and sub-domains
#		sub = sub[1]				# 
		arraymerge[count].append(sortip)
		#temp = ()				# Creates a temp to hold strings with sub-domains
		if sortip == ip_sub[0]:			# If IP-address matches IP-address in IP_SUB
			arraymerge[count].append(ip_sub[1])		# Add string with sub-domain to temp

#old	outfilemerge.write(sortip+'|'+temp)		# Writes to file with format (IP|SUB1,SUB2,SUBx)

with open(dName + '.merged.txt', "w") as f:   	# Writes final merge to this file
	for item in arraymerge:
		f.write("%s\n" % item)		# Writes to file with format (IP|SUB1,SUB2,SUBx)
	




#arraymerge[line] = 
#			arraymerge.append([line][temp])
#				if line not in lines_seen: 
					#lines_seen.add(line)
	#arraymerge.append()
f.close()


