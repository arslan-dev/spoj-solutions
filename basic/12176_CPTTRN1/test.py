

# CPTTRN1 - Character Patterns (Act 1)


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
        t = l%2
        for c in range (0, maxc):
           sys.stdout.write(character_of_type(t))
           t = (t+1) % 2
        sys.stdout.write('\n')
    sys.stdout.write('\n')
