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
    return factors

i = 1
limit = 10000
amicable = []

while i < limit:
    if sum(factors(sum(factors(i))))==i and sum(factors(i)) != i:
        amicable.append(i)
    i+=1

print(sum(amicable))
