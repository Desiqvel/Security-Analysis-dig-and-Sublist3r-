#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy

# Saves argument from user

if len(sys.argv) < 2:
    print("You must parse a website address in the argument")
    sys.exit()

dName = sys.argv[1]

#Global variables

global subdomains, ip, sub, ipandsub, sortip, dub_sort_ip
ip = []
sub = []
ipandsub = []
dub_sort_ip = []
sortip = []
subdomains = []

#

def ipsubs(nyipsub):
    sip, ssub = splitting(nyipsub)
    ip.append(sip)
    sub.append(ssub)

def ipnsub(ipwithsub):
    ipandsub.append(ipwithsub)

def splitting(lines):
    val1, val2 = [i.strip() for i in lines.split('|')]
    return val1, val2

def baresub(nysub):
    sub.append(nysub)

def sortedip_dub(nyip):
    dub_sort_ip.append(nyip)

def sortedip(nyip):
    sortip.append(nyip)

def match(i):
    same = []
    for k in ipandsub:
        sip, ssub = splitting(k)
        if i == sip:
            same.append(ssub)
    str_join = ",".join(same)
    return str_join                 # Remember to remove empty list(send 0 and if else in return)




# Runs sublist3r with the address from the argument
# Makes a .sub.txt file to be used later
subdomains = sublist3r.main(dName, 40, "", ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)


# 	Dig runs sub-addresss and get their IP

# Opens file sublist3r made and preps for a for-loop and checks
for domainName in subdomains:
    domainName = domainName.rstrip()	# Removes whitespaced on the right side
    cmd = ("dig %s +short | grep -P '^(?:(?![a-z]).)*$'" % domainName)	# Runs dig command with regex so only
    ipz = os.popen(cmd).read()						# Useable information gets saved
    ipz = ipz.rstrip()
    ipz = ipz.split('\n')	# Splits the line on newline
    if len(ipz) > 1:		# Checks if there is multiple IP-addresses
        for line in ipz:
            ipandsubx = line + "|" + domainName + "\n" 	# Writes IP-addresses and sub-domains
            ipnsub(ipandsubx)
            ipsubs(ipandsubx)
#ipandsub.append(ipandsubx)
    else:
        ipandsubx = ipz[0] + "|" + domainName + "\n" 	# Writes IP-addresses and sub-domains
        ipnsub(ipandsubx)
        ipsubs(ipandsubx)
#ipandsub.append(ipandsubx)
    ip.append(ipz[0])    				# Writes unsorted IP-addresses



	# These three segment uses lambda and sorted to sort IP-addresses to get the lowest first to a file

# Makes an array with all the sorted IP-addresses

iplist = sorted([i.strip() for i in ip], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))
for i in iplist:
    if len(i.strip()) > 0: 				# Check if the length is greater than zero
        sortedip_dub(i)        		                # Writes the file with sorted IP-addresses 

	# Sort so no duplicates of IP
lines_seen = set() 					# holds lines already seen
for line in dub_sort_ip:
    if line not in lines_seen: 				# not a duplicate
        sortedip(line)
        lines_seen.add(line)


	# Merges IP-addresses and sub-domains
with open(dName + '.finalmerge.csv', "a") as f:     # Writes final merge to this file
    for i in sortip:
        f.write(i + "|" + match(i) + "\n")
#        print(i + '|' + match(i) + "\n")           #test to see output
f.close()

