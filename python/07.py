primes = [2,3,5,7]
x = 9

while len(primes) < 10001:
    p = 0
    for number in primes:
        if x % number == 0:
            p+=1
    if p == 0:
        primes.append(x)
    x+=2

print(max(primes))
