##sieve
import numpy as N

n = 1000000
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

primezero = [y for y in primes if y != 0]
maxprime = [y for y in primes if y != 0]

product = 0
maxproduct = 0
longest = 0
i=0
j=0

while j+i < len(primezero):
    while i < len(primezero)-j:
        product = product + primezero[j+i]
        if product > n:
            i = len(primezero)
        if product > maxproduct and product in maxprime and i > longest:
            maxproduct = product
            longest = i
            maxprime = maxprime[maxprime.index(maxproduct):]        
        i+=1
    j+=1
    i=0
    product=0
        
print(maxproduct)
