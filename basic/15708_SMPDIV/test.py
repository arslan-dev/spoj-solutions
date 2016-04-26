#!/usr/bin/python
#coding=utf-8

# SMPDIV - Divisibility


"""

t - number of test cases


"""

import sys

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line


# PROGRAM STARTS HERE

maxt = int(read_line()) 

for t in range(0, maxt):    
    line = read_line()
    components = line.split(' ')
    n, x, y = int(components[0]), int(components[1]), int(components[2])

    l = lambda bs, b: bs + ' ' + str(b) if b%x==0 and b%y!=0 else bs
    print reduce(l, range(1, n), '').strip()
