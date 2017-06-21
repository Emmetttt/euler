import numpy as np

def factors(n):
    factors  = [1,n]
    j = n
    i = 2
    while i < j:
        if n % i == 0 and i not in factors:
            j = n/i
            factors.append(int(n/i))
            factors.append(i)
        i+=1
    factors.sort()
    return factors

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

prime = primes(int(round(np.sqrt(100000000))))
prime = prime[1:]

def divisor(n):
    div = factors(n)
    newdiv = []
    for d in div:
        d = int(d + n/d)
        if d%2 == 0: #Even not prime
            return False
        
        if d not in newdiv:
            newdiv.append(d)

    prime = primes(int(round(np.sqrt(max(newdiv)))))
    prime = prime[1:]
    for x in newdiv:
        for y in prime:
            if x%y == 0: #If divisible by a prime
                return False
    return True
    
summation = 2
i = 5
while i < 100000000:
    j = 0
    x = True
    while j < len(prime):
        if prime[j] > np.sqrt(i) or i%prime[j] == 0:
            j = len(prime) #terminate loop
            x = False
        j+=1
    if x == True: #i is prime
        if divisor(i-1):
            summation = summation+i
    i+=2
            






