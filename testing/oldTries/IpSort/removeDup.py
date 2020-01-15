#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os

dName = sys.argv[1]

lines_seen = set() # holds lines already seen
outfile = open(dName + '.sortNoDupIP.txt', "w")
for line in open(dName + '.sortedIP.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
