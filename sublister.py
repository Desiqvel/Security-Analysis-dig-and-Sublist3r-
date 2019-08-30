#!/usr/bin/env python3

import sublist3r 
import dig
import sys

dName = sys.argv[1]

print ("Starting to print from " + dName)

subdomains = sublist3r.main(dName, 40, dName + 'sub.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)

ipddr = dig -f dName.txt +short | grep -P '^(?:(?![a-z]).)*$' > dname_ipaddr.txt
