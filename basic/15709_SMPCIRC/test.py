#!/usr/bin/python
#coding=utf-8

# SMPDIV - Divisibility


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

def distance(x1, x2, y1, y2):
    _x = x2-x1
    _y = y2-y1
    return math.sqrt(_x**2 + _y**2)

def diff_square(x, y):
    return (y-x)**2


# PROGRAM STARTS HERE

maxt = int(read_line()) 

for t in range(0, maxt):    
    line = read_line()
    comps = line.split(' ')
    x1, y1, r1, x2, y2, r2 = int(comps[0]), int(comps[1]), int(comps[2]), int(comps[3]), int(comps[4]), int(comps[5])

    d = distance(x1, x2, y1, y2)

    if d+r1 < r2 or d+r2 < r1:
        print 'I'
    elif d+r1 == r2 or d+r2 == r1:
        print 'E'
    else:
        print 'O'

    """
    if distance_square(x1, x2, y1, y2) == diff_square(r2, r1):
        print 'E'
    elif distance_square(x1, x2, y1, y2) < diff_square(r2, r1):
        print 'I'
    else:
        print 'O'
    """
