#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


import sys
import operator

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line

def rotate(vec):
    if vec==(1,0):
        return (0,1)
    elif vec==(0,1):
        return (-1,0)
    elif vec==(-1,0):
        return (0,-1)
    return (1,0)

class Spiral:

    def __init__(self, maxs):
        self.maxs = maxs
        self.data = [['.' for r in range(maxs)] for c in range(maxs)]
        self.make_spiral()

    def make_spiral(self):
        vec = (1,0)
        cur = (0,0)

        second_step = False 

        self.data[cur[0]][cur[1]] = '*'
        while(True):

            if self.is_dead_end(cur, vec) and second_step:
                break

            second_step = False

            r = 0
            while self.is_dead_end(cur, vec) and r<4:
                r+=1
                vec = rotate(vec)
                second_step = True

            if (r>=4):
                break

            cur = tuple(map(operator.add, cur, vec))
            self.data[cur[0]][cur[1]] = '*'

    def is_dead_end(self, cur, vec):
        next_cur = tuple(map(operator.add, cur, vec))
        if next_cur[0]>=self.maxs or next_cur[0]<0 or next_cur[1]>=self.maxs or next_cur[1]<0 or self.data[next_cur[0]][next_cur[1]] == '*':
            return True

        nnc = tuple(map(operator.add, next_cur, vec))
        if nnc[0]>=0 and nnc[0]<self.maxs and nnc[1]>=0 and nnc[1]<self.maxs and self.data[nnc[0]][nnc[1]] == '*':
            return True


    def __repr__(self):
        s = ""
        for r in range(0, self.maxs):
            for c in range (0, self.maxs):
                s += self.data[c][r]
            s += '\n'
        return s

#*********************
# PROGRAM STARTS HERE
#*********************

maxt = int(read_line())

for t in range(0, maxt):
    maxs = int(read_line())

    spiral = Spiral(maxs)
    print spiral
