#!/usr/bin/env python3

import sys
import os
import subprocess
import csv

def split_ip(ip):
    """Split a IP address given as string into a 4-tuple of integers."""
    return tuple(int(part) for part in ip.split('.'))

def my_key(item):
    return split_ip(item[0])

items = sorted(ipCount.items(), key=my_key)
