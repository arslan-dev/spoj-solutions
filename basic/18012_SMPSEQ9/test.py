#!/usr/bin/python
#coding=utf-8

# SMPSEQ9 - Fun with Sequences (Act 7) 

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
s = map(int, read_line().split())[0:maxn]
maxm = int(read_line())
q = map(int, read_line().split())[0:maxm]

avs = reduce(operator.add, s, 0)/float(maxn)
avq = reduce(operator.add, q, 0)/float(maxm)
if (avs > avq):
    print ' '.join(map(str, s))
else:
    print ' '.join(map(str, q))
