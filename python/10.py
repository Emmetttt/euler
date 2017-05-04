##sieve
import numpy as N

n = 2000000
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
    
m = -1

for n in primes:
    if n > 0:
        m = m + n

print(m)
