#!/usr/bin/python
#coding=utf-8

# CHITEST1 - Sum of two numbers

import operator

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line


#*********************
# PROGRAM STARTS HERE
#*********************

maxn = int(read_line())

for n in range(0, maxn):
    comps = read_line().split()
    a, b = float(comps[0]), float(comps[1])
    print '{:g}'.format(a+b)
