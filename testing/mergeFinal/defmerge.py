#!/usr/bin/env python3

import sublist3r 
import subprocess
import sys
import os
import numpy

dName = 'vg.no'

global ip, sub, ipandsub, sortip
ip = []
sub = []
ipandsub = []
sortip = []


def ipsubs(nyipsub):
    sip, ssub = splitting(nyipsub)
    ip.append(sip)
    sub.append(ssub)

def ipnsub(ipwithsub):
    ipandsub.append(ipwithsub)

def splitting(lines):
#    for line in lines:
    val1, val2 = [i.strip() for i in lines.split('|')]
    return val1, val2

def baresub(nysub):
    sub.append(nysub)

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

with open(dName + '.IP_SUB.txt', "r") as k:
    ipsub = [i.strip() for i in k.readlines()]
    for line in ipsub:
        ipsubs(line)
        ipnsub(line)

with open(dName + '.sortNoDupIP.txt', "r") as f:
    allipsorted = [i.strip() for i in f.readlines()]
    for sort in allipsorted:
        sortedip(sort)

with open(dName + '.finalmerge.csv', "a") as f:     # Writes final merge to this file
    for i in sortip:
        f.write(i + "|" + match(i) + "\n")
#        print(i + '|' + match(i) + "\n")           #test to see output
f.close()
