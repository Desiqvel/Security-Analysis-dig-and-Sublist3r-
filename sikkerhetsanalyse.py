#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy
import csv

#Global variables

global subdomains, subdomainsdub, ip, sub, ipandsub, sortip, dub_sort_ip
ip = []
sub = []
ipandsub = []
dub_sort_ip = []
sortip = []
subdomains = []
subdomainsdub = []

	# Makes sure user doesn't parse too many og few arguments

if len(sys.argv) < 2:
    print("You must parse a website address in the argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many arguments, only one website address at the time")
    sys.exit()

dName = sys.argv[1] 		# Saves argument from user


	# Removes outputerror from sublist3r
	# Comment out class with call to debug
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()



def ipsubs(nyipsub):		# Adds IP, subdomain and both together
    ipandsub.append(nyipsub)
    sip, ssub = splitting(nyipsub)
    ip.append(sip)
    sub.append(ssub)

def dub(var):			# Sort so no duplicates
    lines_seen = set() 				# holds lines already seen
    for line in var:
        if line not in lines_seen:		# not a duplicate
            lines_seen.add(line)
    return lines_seen

def nosub():			# If no subdomains was found, prints out message
    if len(sub) < 1: 
        print("No sub adresses found, exits")
        sys.exit()

def splitting(lines):		# Splits IP-address and subdomain
    val1, val2 = [i.strip() for i in lines.split('|')]
    return val1, val2

def nydomaindub(nydom):		# Adds a new possible duplicate subdomain
    subdomainsdub.append(nydom)

def nydomain(nydom):		# Adds a new subdomain
    subdomains.append(nydom)

def sortedip_dub(nyip):		# Adds a new unsorted IP-address
    dub_sort_ip.append(nyip)

def sortedip(nyip):		# Adds a new sorted IP-address
    sortip.append(nyip)

def match(i):			# Maches sorted IP-address to subdomain
    same = []					# Temp that stores subdomains to a common IP 
    for k in ipandsub:
        sip, ssub = splitting(k)		# Splits Ip and Sub so both variables are easy accessible
        if i == sip:
            same.append(ssub)
    str_join = ",".join(same)			# Joins subdomains list in one string
    if same == '':				# Checks if list is empty
        return False 				# Returns False if no subdomains matches any IP
    else:
        return str_join

print("Starts Sublist3r - Searches for subdomains\n")

	# Runs sublist3r with the address from the argument
subdomainsz = sublist3r.main(dName, 40, "", ports= None, silent= True, verbose= False, enable_bruteforce= False, engines=None)

for domainName in subdomainsz:
    var = domainName.split('<BR>')
    if len(var) > 1:
        for i in var:
            nydomaindub(i)
    else:
        nydomaindub(domainName)

	# Remove subdomain duplicates
dubdom = dub(subdomainsdub)
for lines in dubdom:
    nydomain(lines)


print("Sublist3r finished\n")
print("Starts Dig - searches for IP-addresses\n")

	# Opens the sublist3r list and uses dig to get IP-addresses
for domainName in subdomains:
    domainName = domainName.rstrip()		# Removes whitespaced on the right side
    cmd = ("dig @8.8.8.8 %s +short | grep -P '^(?:(?![a-z]).)*$'" % domainName)	# Runs dig command with regex so only
    if cmd:                    			# Checks if IP address was found
        ipz = os.popen(cmd).read()		# Useable information gets saved
        ipz = ipz.rstrip()
        ipz = ipz.split('\n')			# Splits the line on newline
        if len(ipz) > 1:			# Checks if there is multiple IP-addresses
            for line in ipz:
                ipandsubx = line + "|" + domainName + "\n" 	# Writes IP-addresses and sub-domains
                ipsubs(ipandsubx)
        else:
            ipandsubx = ipz[0] + "|" + domainName + "\n" 	# Writes IP-addresses and sub-domains
            ipsubs(ipandsubx)


print("Dig finished - Sorting IP-addresses\n")

	# This segment uses lambda and sorted to sort IP-addresses to get the lowest first to a file
	# Makes an array with all the sorted IP-addresses
iplist = sorted([i.strip() for i in ip], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))
for i in iplist:
    if len(i.strip()) > 0:			# Check if the length is greater than zero
        sortedip_dub(i)   	                # Writes the file with sorted IP-addresses 

	# Removes duplicates
dubip = dub(dub_sort_ip)
for lines in dubip:
    sortedip(lines)

print("Finished sorting IP-addresses - Matches IP-addresses and subdomains\n")

	# Merges IP-addresses and sub-domains, makes a .csv file
with open(dName + '_IP_domains.csv', "a") as csv_file:     # Writes final merge to this file
    fieldnames = ['IP', 'Sub_domain']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in sortip:
        var = match(i)
        if var != False:
            writer.writerow({'IP': i, 'Sub_domain': var})
csv_file.close()

print("Script done! Output written to " + dName + "_IP_domains.csv")

	# Writes to .txt format

#with open(dName + '_IP_domains.txt', "a") as f:     # Writes final merge to this file
#    for i in sortip:
#        var = match(i)
#        if var != False:
#            f.write(i + "|" + var + "\n")
#        print(i + '|' + match(i) + "\n")           #test to see output
#f.close()
#print("Script done! Output written to " + dName + "_IP_domains.txt")

