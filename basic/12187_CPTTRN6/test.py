

# CPTTRN6 - Character Patterns (Act 6)


import sys

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl, maxc = int(params[0]), int(params[1])
    maxl1, maxc1 = maxl+1, maxc+1
    maxh, maxw = int(params[2]), int(params[3])
    maxh1, maxw1 = maxh+1, maxw+1
    maxh2, maxw2 = maxh+2, maxw+2
    maxresl, maxresc = maxl1*maxh1, maxc1*maxw1
    res = [['.' for c in range(maxresc)] for l in range(maxresl)]

    for l in range (0, maxl1):
        for c in range (0, maxc1):

            for x in range (0, maxw):
                res[l*maxh1 + maxh][c*maxw1 + x] = '-'
            for y in range (0, maxh):
                res[l*maxh1 + y][c*maxw1 + maxw] = '|'
            res[l*maxh1 + maxh][c*maxw1 + maxw] = '+'
            
    for l in range(0, maxresl-1):
        for c in range (0, maxresc-1):
            sys.stdout.write(res[l][c])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
