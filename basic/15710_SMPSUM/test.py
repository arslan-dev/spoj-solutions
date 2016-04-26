#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


import sys
import math

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line


# PROGRAM STARTS HERE

comps = read_line().split(' ')
a, b = int(comps[0]), int(comps[1])

s = 0
for i in range(a, b+1):
    s += i**2

print s
