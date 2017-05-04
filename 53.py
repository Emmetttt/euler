def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def NCR(n,r):
    return (factorial(n))/(factorial(r) * factorial(n-r))

n = 23
r = 10
comb = 0

while n < 101:
    while r < (n-1):
        if NCR(n,r) > 1000000:
            comb+=1
        r+=1
    n+=1
    r=2
