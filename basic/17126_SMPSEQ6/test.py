#!/usr/bin/python
#coding=utf-8

# SMPSEQ6 - Fun with Sequences (Act 4)


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

comps = read_line().split()
maxn, x = int(comps[0]), int(comps[1])
s = map(int, read_line().split())[0:maxn]
q = map(int, read_line().split())[0:maxn]

r = []
for i in range(0, maxn):
    for y in range(max(0, i-x), min(maxn, i+x+1)):
        if s[i] == q[y]:
            r.append(i+1)
            break

print ' '.join(map(str, r))
