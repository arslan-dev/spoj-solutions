

# HS12HDPW - Hidden Password 


"""

t - number of test cases
n - number of 6-tuples


"""

import sys

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line


# PROGRAM STARTS HERE

maxt = int(read_line()) 

for t in range(0, maxt):    
    n = int(read_line())
    line = read_line()
    symbols = read_line()
    components = line.split(' ')
    result = ''
    for i in range(0, n):
        word = components[i]
        b1, b2 = '', ''
        for c in range(0, 6):
            char = word[c]
            ascii_code = ord(char)
            #sys.stdout.write('{:^3} {:>4} = {:0>8b}b\n'.format(char, ascii_code, ascii_code))
            bit1 = (ascii_code >> c) & 1
            b1 += str(bit1)

            c2 = (c+3) % 6
            bit2 = (ascii_code >> c2) & 1
            b2 += str(bit2)
        b1 = b1[::-1]
        p1ci = int(b1, 2)
        b2 = b2[::-1]
        p2ci = int(b2, 2)
        result += symbols[p1ci] + symbols[p2ci]

    print result
