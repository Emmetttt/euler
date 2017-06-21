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
