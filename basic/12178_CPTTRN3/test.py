

# CPTTRN3 - Character Patterns (Act 3)


import sys

def character_of_type(t):
   return '*' if t==1 else '.'

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl, maxc = int(params[0]), int(params[1])
    maxresl, maxresc = 3*maxl + 1, 3*maxc + 1
    res = [[0 for c in range(maxresc)] for l in range(maxresl)]

    for l in range (0, maxl):
        for c in range (0, maxc):
            
            for i in range (0, 4):
                res[(l+0)*3][c*3 + i] = 1
                res[(l+1)*3][c*3 + i] = 1
                res[l*3 + i][(c+0)*3] = 1
                res[l*3 + i][(c+1)*3] = 1

    for l in range(0, maxresl):
        for c in range (0, maxresc):
            sys.stdout.write(character_of_type(res[l][c]))
        sys.stdout.write('\n')
    sys.stdout.write('\n')
