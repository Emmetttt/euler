import numpy as np

##Calculate primes##
def primes(n):
    i = 2
    while i < np.sqrt(n)+1:
        if n%i == 0:
            return False
        i+=1
    return True


##Calculate Diagnals##
def diagnals(k):
    i=3
    diags = 1
    diff = k - 1
    diagnum = [k**2, k**2-diff, k**2-(2*diff), k**2-(3*diff)]

    diagnum.sort()
    return diagnum

##Compare Diagnals##

numerator = 0
denominator = 1
i = 3

while True:
    for diag in diagnals(i):
        denominator+=1
        if primes(diag) == True:
            numerator+=1
    if numerator/denominator < 0.1:
        print("ratio: ", numerator/denominator, "\nSide length: ", i, "\n")
        break
    i+=2

