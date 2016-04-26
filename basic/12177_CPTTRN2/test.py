

# CPTTRN2 - Character Patterns (Act 2)


import sys

def character_of_type(t):
   return '*' if t==0 else '.'

n = raw_input() 
n = int(n)

for i in range(0, n):
    line = raw_input()
    params = line.split(' ')
    maxl = int(params[0])
    maxc = int(params[1])

    for l in range (0, maxl):
        for c in range (0, maxc):
            t = not( (l==0) or (l==maxl-1) or (c==0) or (c==maxc-1) )
            sys.stdout.write(character_of_type(t))
        sys.stdout.write('\n')
    sys.stdout.write('\n')
