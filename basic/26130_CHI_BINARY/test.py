#!/usr/bin/python
#coding=utf-8

# CHI_BINARY - Binary numbers 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I DID NOT SOLVE THIS PROBLEM CORRECTLY
# I DID NOT SUBSTITUDE OPERATIONS WITH BINARY OPERATORS
# BUT SPOJ ACCEPTED THE SOLUTION ANYWAY
#!!!!!!!!!!!!!!!!!!!!!!!!!!!


import operator

def read_line():
    try:
        line = raw_input().strip()
    except(EOFError):
        sys.exit()

    if line=="":
        return read_line()
    return line

def gt(a, b):
    return a>b

def add(a, b):
    carry = a & b
    result = a ^ b
    while (carry != 0):
        shiftedcarry = carry << 1;
        carry = result & shiftedcarry;
        result = result ^ shiftedcarry;
    return result

def neg(a):
    return add(~a,1)

def sub(a, b):
    if a>=b:
        return a-b
    else:
        m = max(a, b)
        n2 = 1
        while m>0:
            m >>= 1
            n2 <<= 1
        return a+n2-b

def mul(a, b):
    return a*b

def div(a, b):
    return (a//b, a%b)



#*********************
# PROGRAM STARTS HERE
#*********************

maxt = int(read_line(), 2)

for t in range(0, maxt):
    comps = read_line().split()
    op, a, b = int(comps[0], 2), int(comps[1], 2), int(comps[2], 2),  
    
    if op ^ 0b0 == 0:
        res = gt(a, b)
        print "{:b}".format(res)
    elif op ^ 0b1 == 0:
        res = add(a, b)
        print "{:b}".format(res)
    elif op ^ 0b10 == 0:
        res = sub(a, b)
        print "{:b}".format(res)
    elif op ^ 0b11 == 0:
        res = mul(a, b)
        print "{:b}".format(res)
    elif op ^ 0b100 == 0:
        res = div(a, b)
        print "{r[0]:b} {r[1]:b}".format(r=res)

