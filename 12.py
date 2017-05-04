def divisor(n):
    factors  = [1, n]
    j = n
    i = 2
    while i < j:
        if n % i == 0:
            j = n/i
            factors.append(n/i)
            factors.append(i)
        i+=1
    return factors

i = 2
triangle = 1

while len(divisor(triangle)) < 500:
    triangle = triangle + i
    i+=1
