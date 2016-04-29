#!/usr/bin/python
#coding=utf-8

# SMPSEQ5 - Fun with Sequences (Act 3)


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

r = []
for i in range(0, min(maxn, maxm)):
    if s[i] == q[i]:
        r.append(i+1)

print ' '.join(map(str, r))
