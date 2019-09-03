#!/usr/bin/env python3

import sublist3r
import sys
import os
import subprocess


from collections import namedtuple
ip_type = namedtuple("IP", 'g1 g2 g3 g4 port')

def to_ip(string: str) -> ip_type:
    groups, port = string.split('|')
    g1, g2, g3, g4 = [int(g) for g in groups.split('.')]
    return ip_type(g1, g2, g3, g4, int(port) )

array = [['IP', 'SUB']]


with open('nrk.noipaddr.txt') as IPdom:
        for line in IPdom:
                #line = line.rstrip('\n')
#                var = line.split( '|' )
                array.append(line)

print(sorted(array, key=to_ip))
