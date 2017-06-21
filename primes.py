##sieve
import numpy as np
import itertools

def primes(n):
    primes = np.arange(1,n+1,1).tolist()

    p = 2
    i = 2
    k = 1
    x = True

    while k < np.sqrt(n)+1:
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

    return [y for y in primes if y != 0]

prime = primes(int(round(np.sqrt(987654321))))  #Largest factor of any
                                                #0-9 pandigital prime
prime = prime[1:] #Take 1 as not a prime

def primecheck(n):
    for x in prime:
        if n%x == 0 and n!=x:
            return False
        if x > n:
            return True
    return True

print(prime)