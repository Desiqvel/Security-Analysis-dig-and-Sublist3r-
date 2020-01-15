#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy

dName = 'vg.no'

#arraymerge = []
#outfilemerge = open(dName + '.merged.txt', "w")        # Writes final merge to this file

with open(dName + '.IP_SUB.txt', "r") as k:
  with open(dName + '.sortNoDupIP.txt', "r") as sortip:   # Opens sorted IP-addresses
    with open(dName + '.hvaer.txt', "a") as f:     # Writes final merge to this file
      for allip in sortip:
        match = ""
        ip = ""
        sub = ""
        helpme = ""
        kk = []
        for ipsub in k:
#       kk = list(k)
#        ipsub = ipsub.read()
          ip, sub = ipsub.split('|')
#          sub = kk[1]
#          ip = kk[0]
#          f.write("%s|%s" % (ip, sub))
#        for item in ip:
#          if len(ip.strip()) > 0:		#checks if no line
#          helpme = helpme + allip
          
          if allip == ip:
            match.append(sub)
#        str1 = ''.join(match)
        
        f.write("{}".format(allip) + "|" + "{}".format(match))
#        f.write(allip + '<-ip' + '|' + 'sub->' + str1) # + '\n') 


#        f.write("%s\n" % allip) 

f.close()
