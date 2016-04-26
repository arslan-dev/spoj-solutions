

# STRHH - Half of the hal
# feifjalaelfjal:


import sys

n = raw_input() 
n = int(n)

for i in range(0, n):
    s = raw_input()
    maxi = len(s) / 2

    res = ""
    for i in range(0, maxi, 2):
        res += s[i]
    print res
