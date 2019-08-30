#!/usr/bin/env python3

import sublist3r 
#import dig
import sys
import os

#dName = sys.argv[1]
line = ("elasticsearch5.anbefaling.nrk.no")
dName = ("testNRK")
#myCmd = ("dig elasticsearch5.anbefaling.nrk.no +short | grep -P '^(?:(?![a-z]).)*$' > test2.txt")
myCmd = ("dig %s +short | grep -P '^(?:(?![a-z]).)*$' >> %sipaddr.txt" % (line, dName))

os.system(myCmd)

