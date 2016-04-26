#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


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


# PROGRAM STARTS HERE

x = int(read_line())
wow = 'W' + 'o'*x + 'w'
print wow
