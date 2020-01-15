#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os

#Makes files to run independent tests


# Saves argument from user

if len(sys.argv) < 2:
    print("You must parse a website address in the argument")
    sys.exit()

dName = sys.argv[1]


# Runs sublist3r with the address from the argument
# Makes a .sub.txt file to be used later
subdomains = sublist3r.main(dName, 40, dName + '.sub.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)


try:
    f = open(dName + '.sub.txt')
    f.close()
except FileNotFoundError:
    print('File does not exist, no subdomains found')
    sys.exit()

# checks if file is accessible
try:
    f = open(dName + '.sub.txt')
    f.close()
except IOError:
    print('File is not accessible')
    sys.exit()

# 	Dig runs sub-addresss and get their IP

ofName = dName + ".IP_SUB.txt"
outputFile = open(ofName, "w") 	# Makes new file with IP | SUB-DOMAIN
iplist = dName + ".IPunsort.txt"
outputIP = open(iplist, "w") 	# Makes new file with the unsorted IP-addresses

with open(dName + '.sub.txt') as text_file: 	# Opens file sublist3r made and preps for a for-loop and checks
    for domainName in text_file:
        domainName = domainName.rstrip()	# Removes whitespaced on the right side
        cmd = ("dig %s +short | grep -P '^(?:(?![a-z]).)*$'" % domainName)	# Runs dig command with regex so only
        ip = os.popen(cmd).read()						# Useable information gets saved
        ip = ip.rstrip()
        ip = ip.split('\n')	# Splits the line on newline
        if len(ip) > 1:		# Checks if there is multiple IP-addresses
            for line in ip:
                outputFile.write(line+"|"+domainName+"\n") 	# Writes IP-addresses and sub-domains
        else:
            outputFile.write(ip[0]+"|"+domainName+"\n")

        outputIP.write(ip[0]+"\n") 				# Writes unsorted IP-addresses


outputFile.close()
outputIP.close()
text_file.close()

	# These three segment uses lambda and sorted to sort IP-addresses to get the lowest first to a file

with open(dName + '.IPunsort.txt', "r") as infile: 	# Makes an array with all the sorted IP-addresses
	iplist = sorted([i.strip() for i in infile.readlines()], key = lambda x: int(''.join((lambda a:lambda v:a(a,v))(lambda s,x: x if len(x) == 3 else s(s, '0'+x))(i) for i in x.split('.'))))


with open(dName + ".unsIP.txt", "w") as outfile: 	# Writes the file with sorted IP-addresses 
	outfile.write("\n".join(i for i in iplist))


							# Check if the length is greater than zero
with open(dName + ".unsIP.txt", 'r') as inp, open(dName + '.sortedIP.txt', 'w') as out:
	for line in inp:
		if len(line.strip()) > 0:
			out.write(line)

infile.close()
outfile.close()


	# Sort so no duplicates of IP
lines_seen = set() 					# holds lines already seen
outfiledup = open(dName + '.sortNoDupIP.txt', "w")
for line in open(dName + '.sortedIP.txt', "r"):
    if line not in lines_seen: 				# not a duplicate
        outfiledup.write(line)
        lines_seen.add(line)
outfiledup.close()

	# Merges IP-addresses and sub-domains
