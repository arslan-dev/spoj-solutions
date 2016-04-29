#!/usr/bin/python
#coding=utf-8

# PCROSS2 - Cross Pattern (Act 2)

import sys

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

maxt = int(read_line())

for t in range(0, maxt):
    comps = read_line().split(' ')
    maxr, maxc, sr, sc = int(comps[0]), int(comps[1]), int(comps[2])-1, int(comps[3])-1

    res = [['.' for r in range(maxr)] for c in range(maxc)]

    for s in range(0, min(maxr-sr, maxc-sc)):
        res[sc+s][sr+s] = '*'
    for s in range(1, min(sr+1, sc+1)):
        res[sc-s][sr-s] = '*'
    for s in range(1, min(maxr-sr, sc+1)):
        res[sc-s][sr+s] = '*'
    for s in range(1, min(sr+1, maxc-sc)):
        res[sc+s][sr-s] = '*'

    for r in range(0, maxr):
        for c in range (0, maxc):
            sys.stdout.write(res[c][r])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
