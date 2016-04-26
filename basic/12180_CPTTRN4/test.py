

# CPTTRN4 - Character Patterns (Act 4)


import sys

def character_of_type(t):
   return '*' if t==1 else '.'

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl, maxc = int(params[0]), int(params[1])
    maxh, maxw = int(params[2]), int(params[3])
    maxh1, maxw1 = maxh+1, maxw+1
    maxh2, maxw2 = maxh+2, maxw+2
    maxresl, maxresc = maxh1*maxl + 1, maxw1*maxc + 1
    res = [[0 for c in range(maxresc)] for l in range(maxresl)]

    for l in range (0, maxl):
        for c in range (0, maxc):
            
            for y in range (0, maxh2, maxh1):
                for x in range (0, maxw2):
                    res[l*maxh1 + y][c*maxw1 + x] = 1
            for x in range (0, maxw2, maxw1):
                for y in range (0, maxh2):
                    res[l*maxh1 + y][c*maxw1 + x] = 1

    for l in range(0, maxresl):
        for c in range (0, maxresc):
            sys.stdout.write(character_of_type(res[l][c]))
        sys.stdout.write('\n')
    sys.stdout.write('\n')
