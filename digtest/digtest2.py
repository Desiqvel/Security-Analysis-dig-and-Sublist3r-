#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess

dName = sys.argv[1]

ofName = dName + "output.txt"
outputFile = open(ofName, "w")
with open(dName + 'sub.txt') as text_file:
    for domainName in text_file:
        #ip = os.system("dig %s +short")
        domainName = domainName.rstrip()
        cmd = ("dig %s +short" % domainName)
        #ip = subprocess.check_output([cmd])
        ip = os.popen(cmd).read()
        #ip = subprocess.check_output(["dig", "%s", "+short", "% domainName"])
        #print("DOMAIN:>"+domainName+", IP: >"+ip+"<")
        ip = ip.rstrip()
        outputFile.write("Domain:>"+domainName+", IP:>"+ip+"<")
        
        #outputFile.write('\n')
        #exit()

        

        
outputFile.close()
text_file.close()
