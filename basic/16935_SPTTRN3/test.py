#!/usr/bin/python
#coding=utf-8

# SMPSUM - Iterated sums


import sys
import operator
import math

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line

def rotate(vec, angle):
    x = vec[0]
    y = vec[1]
    return [int(x*math.cos(angle) - y*math.sin(angle)), int(x*math.sin(angle) + y*math.cos(angle))]

from enum import Enum
class Task(Enum):
    Move = 1
    Break = 2

class Spiral:

    def __init__(self, maxs):
        self.maxs = maxs
        self.data = [['.' for r in range(maxs)] for c in range(maxs)]
        self.program = [Task.Move, Task.Move, Task.Move, Task.Move, Task.Break]
        self.make_spiral()

"""
    def make_spiral(self):
        vec = [1,0]
        cur = [0,0]

        program_pointer = 0
        rotation_direction = +1
        steps = 0 

        self.sprial_for_cursor(vec, cur, program_pointer, rotation_direction, steps)

    def spiral_for_cursor(self, vec, cur, program_pointer, rotataion_direction, steps):

        if self.is_dead_end(cur, vec):
            return false

        self.data[cur[0]][cur[1]] = '*'

        next_cur = map(operator.add, cur, vec)
        res = spiral_for_cusor(vec, next_cur, program_pointer, rotataion_direction, steps+1)
        if res:
            return res

        next_vec = rotate(vec, rotation_direction * math.pi/2)
        next_cur = map(operator.add, cur, next_vec)
        next_program_pointer = (program_pointer+1)%5
        next_task = self.program[next_program_pointer]
        if next_task == Task.Break:
            next_rotation_direction = (-1) * rotation_direction
        res = spiral_for_cursor(next_vec, next_cur, next_program_pointer, next_rotation_direction, 0)
        if res:
            return res

        self.data[cur[0]][cur[1]] = '.'
        return false

"""
"""
        steps += 1

        if (current_task == Task.Break and steps==2) or self.is_dead_end(cur, vec):

            vec = rotate(vec, rotation_direction * math.pi/2)
            if self.is_dead_end(cur, vec):
                break

            if current_task == Task.Break:
                rotation_direction *= -1

            steps = 0

""" 
    def is_cursor_a_star(self, cur):
        return cur[0]>=0 and cur[0]<self.maxs and cur[1]>=0 and cur[1]<self.maxs and self.data[cur[0]][cur[1]] == '*'

    def is_dead_end(self, cur, vec):
        next_cur = map(operator.add, cur, vec)
        if next_cur[0]>=self.maxs or next_cur[0]<0 or next_cur[1]>=self.maxs or next_cur[1]<0 or self.data[next_cur[0]][next_cur[1]] == '*':
            return True

        nnc = map(operator.add, next_cur, vec)
        if self.is_cursor_a_star(nnc):
            return True
        right_path = map(operator.add, cur, rotate(vec, math.pi/2))
        if self.is_cursor_a_star(right_path):
            return True
        left_path = map(operator.add, cur, rotate(vec, -math.pi/2))
        if self.is_cursor_a_star(left_path):
            return True

        return False


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
