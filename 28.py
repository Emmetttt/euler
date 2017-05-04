import numpy as N

##Calculate Diagnals##
def diagnals(k):
    i=3
    diags = 1
    diagnum = []
    j = 0

    while i < k**2:
        diags = i**2
        while j < 4:
            diagnum.append(diags - (j*(i-1)))
            j+=1
        i+=2
        j=0

    diagnum.sort()
    return diagnum

##Calculate primes##
def primes(n):
    primes = N.arange(1,n+1,1).tolist()

    p = 2
    i = 2
    k = 1
    x = True

    while k < N.sqrt(n)+1:
        p = primes[k]
        if p > 1:
            j = max(primes)
            #while i < j/p+1:
            while ((p*i)-1) < j:
                primes[(i*p)-1] = 0
                i+=1
        i=2
        if k > 1:
            k+=2
        else:
            k+=1

    primes = [y for y in primes if y != 0]
    return primes
##Compare Diagnals##

numerator = 0
i = 3

while i < 100:
    diagnum = diagnals(i)
    p = primes(max(diagnum))
    for diag in diagnum:
        if diag in p:
            numerator+=1
    print(numerator/(len(diagnum)+1))
    if numerator/(len(diagnum)+1) < 0.1:
        break
    i+=1
    numerator=0

print("ratio: ", numerator/(len(diagnum)+1))
