#!/usr/bin/env python3

import sublist3r 
#import dig
import sys
import os

dName = sys.argv[1]

print ("Starting to print from " + dName)

subdomains = sublist3r.main(dName, 40, dName + 'sub.txt', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)

#cmd='dig -f dName.txt +short | grep -P '^(?:(?![a-z]).)*$' > dname_ipaddr.txt'

#myCmd = 'dig -f dNamesub.txt +short > dNameipaddr.txt'

myCmd = ("dig -f %Ssub.txt +short > %Iipaddr.txt" % (dName, dName))

#ipaddrun = dig -f dNamesub.txt +short 
for i in myCmd:
  print(i)
