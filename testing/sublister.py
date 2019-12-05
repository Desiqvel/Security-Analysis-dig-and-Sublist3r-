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

#myCmd = ("dig -f %ssub.txt +short > %sipaddr.txt" % (dName, dName))


#os.system(myCmd)

#grep -P '^(?:(?![a-z]).)*$'





#with open(dName + 'sub.txt') as text_file, open(dName + 'ipaddr.txt', 'w') as myfile:  

#myfile = open(dName + 'sub.txt', 'w')

#for line in text_file:
#	myfile.writelines(text_file)
	
#	myfile.write("Now the file has more content!")

#myfile.close()
#text_file.close()


