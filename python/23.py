def factors(n):
    factors  = [1]
    j = n
    i = 2
    while i < j:
        if n % i == 0:
            j = n/i
            if j != i:
                factors.append(n/i)
                factors.append(i)
            else:
                factors.append(i)
        i+=1
    x = sum(factors)
    if x < n:
        return 0
    if x == n:
        return 1
    if x > n:
        return 2

a = list(range(1, 29000))
b = []
limit = 29000
i = 2
j = 0

while i < limit:
    if factors(i) == 2:
        b.append(i)
        #while j < len(b) and (j*i < limit-1):
        while j < len(b) and b[j]+i < limit:
            x = b[j]+i
            a[x-1] = 0
            j+=1
    j=0
    i+=1
