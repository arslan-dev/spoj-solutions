#!/usr/bin/python
#coding=utf-8

# SMPSEQ8 - Fun with Sequences (Act 6)

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

sums = reduce(operator.add, s, 0)
sumq = reduce(operator.add, q, 0)
if (sums > sumq):
    print ' '.join(map(str, s))
else:
    print ' '.join(map(str, q))
