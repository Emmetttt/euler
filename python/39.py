import math

def perim(a,b):
    return a + b + math.sqrt(a**2 + b**2)

def soltns(p):
    a = 1
    b = 2
    total = 0
    while math.sqrt(a**2 + b**2) < p/2:
        while a < b:
            if perim(a,b) == p:
                total+=1
            a+=1
        b+=1
        a=1
    return total

i = 3
largestperm = 0
largesti = 0

while i < 1001:
    if soltns(i) > largestperm:
        largestperm =soltns(i)
        largesti = i
    i+=1
