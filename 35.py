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

x = [y for y in primes if y != 0]
x=x[7:]

def rot(x):
    x = str(x)
    num = []
    for n in x:
        if int(n)%2 == 0:
            return False
        num.append(n)
    y = []
    i=1
    while i < len(x)+1:
        num = num[-1:] + num[0:len(num)-1]
        if primes[int(''.join(num))-1] == 0:
            return False
        y.append(''.join(num))
        i+=1
    return True

circ = 6

for n in x:
    if rot(n):
        print(n)
        circ+=1
