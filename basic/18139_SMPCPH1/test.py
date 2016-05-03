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
s = read_line()

keys = {}
for n in range(0, maxn):
    keys[s[n]] = s[(n+1)%maxn]

maxm = int(read_line())

for m in range(0, maxm):
    line = read_line()
    res = map(lambda x: keys[x] if keys.has_key(x) else x, line)
    print ''.join(res)
