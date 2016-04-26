

# CPTTRN5 - Character Patterns (Act 5)


import sys

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl, maxc = int(params[0]), int(params[1])
    maxs = int(params[2])
    maxs1 = maxs+1
    maxresl, maxresc = maxs1*maxl + 1, maxs1*maxc + 1
    res = [['.' for c in range(maxresc)] for l in range(maxresl)]

    for l in range (0, maxl):
        for c in range (0, maxc):
            
            for i in range (0, maxs+2):
                res[(l+0)*maxs1][c*maxs1 + i] = '*'
                res[(l+1)*maxs1][c*maxs1 + i] = '*'
                res[l*maxs1 + i][(c+0)*maxs1] = '*'
                res[l*maxs1 + i][(c+1)*maxs1] = '*'

            t = (l+c) % 2
            for i in range (1, maxs1):
                y = l*maxs1 + i
                if t==0:
                    res[y][c*maxs1 + i] = '\\'
                else:
                    res[y][c*maxs1 + maxs1-i] = '/'

            t = (t+1) % 2

    for l in range(0, maxresl):
        for c in range (0, maxresc):
            sys.stdout.write(res[l][c])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
