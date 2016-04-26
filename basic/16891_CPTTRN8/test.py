#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


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
    maxr, maxc, maxs = int(comps[0]), int(comps[1]), int(comps[2])

    maxs2 = maxs*2
    maxresr, maxresc = maxs2*maxr, maxs2*maxc
    res = [['.' for c in range(maxresc)] for r in range(maxresr)]

    for r in range (0, maxr):
        for c in range (0, maxc):
            x, y = c*maxs2 + maxs, r*maxs2 + maxs

            for sy in range(0, maxs):
                for sx in range (0, maxs-sy):
                    res[y+sy][x+sx] = '/' if sx==maxs-sy-1 else '*'
                    res[y+sy][x-sx-1] = '\\' if sx==maxs-sy-1 else '*'
                    res[y-sy-1][x+sx] = '\\' if sx==maxs-sy-1 else '*'
                    res[y-sy-1][x-sx-1] = '/' if sx==maxs-sy-1 else '*'

            
    for r in range(0, maxresr):
        for c in range (0, maxresc):
            sys.stdout.write(res[r][c])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
