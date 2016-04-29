#!/usr/bin/python
#coding=utf-8

# PCROSS1 - Cross Pattern (Act 1)


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

b = False
for i in range(0, maxn):
    b = True
    tmp = s[0]
    for j in range(1, i+1):
        if s[j]>=tmp:
            b = False
            break
        tmp = s[j]

    if b==False:
        continue

    for j in range(i+2, maxn):
        if s[j]<=tmp:
            b = False
            break
        tmp = s[j]

    if b==True:
        break

rs = 'Yes' if b else 'No'
print rs
