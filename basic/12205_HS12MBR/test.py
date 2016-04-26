

# HS12MBR - Minimum Bounding Rectangle


"""

t - number of test cases
n - number of objects

p x y - point
c x y r - circle
l x1 y1 x2 y2 - line segment

output
rect lx ly ux uy


"""

class Rect:
    lp = (0, 0)
    hp = (0, 0)

    def __init__(self, lp, hp):
        self.lp = lp
        self.hp = hp

    def __str__(self):
        return '{lp[0]} {lp[1]} {hp[0]} {hp[1]}'.format(lp=self.lp, hp=self.hp)

import sys

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()
    if line=="":
        return read_line()
    return line

def bounding_box_from_line(line):
    components = line.split(' ')
    rect = Rect((0, 0), (1, 1))
    if components[0]=='p':
        x = int(components[1])
        y = int(components[2])
        rect = Rect((x, y), (x, y))
    elif components[0]=='c':
        x = int(components[1])
        y = int(components[2])
        r = int(components[3])
        rect = Rect((x-r, y-r), (x+r, y+r))
    elif components[0]=='l':
        x1 = int(components[1])
        y1 = int(components[2])
        x2 = int(components[3])
        y2 = int(components[4])
        rect = Rect((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))
    
    return rect

def bounding_box_from_rects(rects):
    r = rects[0]
    minlp = r.lp
    maxhp = r.hp

    for r in rects:
        minlp = (min(minlp[0], r.lp[0]), min(minlp[1], r.lp[1]))
        maxhp = (max(maxhp[0], r.hp[0]), max(maxhp[1], r.hp[1]))

    return Rect(minlp, maxhp)


# PROGRAM STARTS HERE

maxt = int(read_line()) 

for t in range(0, maxt):    
    n = int(read_line())
    rects = []
    for i in range(0, n):
        line = raw_input()
        r = bounding_box_from_line(line)
        rects.append(r)
    print bounding_box_from_rects(rects)
