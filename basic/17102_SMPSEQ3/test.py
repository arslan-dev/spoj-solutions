#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


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

r = filter(lambda x: not (x in q), s)
print ' '.join(map(str, r))
