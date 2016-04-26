

# CPTTRN7 - Character Patterns (Act 7)


import sys

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl, maxc = int(params[0]), int(params[1])
    maxs = int(params[2])
    maxs2 = maxs*2
    maxresl, maxresc = maxs2*maxl, maxs2*maxc
    res = [['.' for c in range(maxresc)] for l in range(maxresl)]

    for l in range (0, maxl):
        for c in range (0, maxc):

            for s in range(0, maxs):
                x, y = c*maxs2, l*maxs2
                res[y+maxs+s][x+s] = '\\'
                res[y+s][x+maxs+s] = '\\'
                res[y+maxs-1-s][x+s] = '/'
                res[y+maxs+maxs-1-s][x+maxs+s] = '/'
            
    for l in range(0, maxresl):
        for c in range (0, maxresc):
            sys.stdout.write(res[l][c])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
