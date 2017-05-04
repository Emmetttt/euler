##sieve
import numpy as N

n = 100000
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

##primes = [y for y in primes if y != 0]

##
def quad(n,a,b):
    return (n**2 + (a*n) + b)

def qp(n,a,b,count=0):
    if primes[quad(n,a,b)-1] != 0:
        return qp(n+1,a,b,count+1)
    else:
        return count-1

a=-1000
b=1
count=0
largest=0
product=0
n=0

while a < 1000:
    while b < 1000:
        if primes[b-1] != 0:
            if qp(n,a,b) > largest:
                largest = qp(n,a,b)
                product = a*b
                print(a,b,largest)
        n=0
        count=0
        b+=1
    n=0
    b=1
    a+=1
