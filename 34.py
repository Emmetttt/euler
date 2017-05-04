def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

i = 145
digits = []
total = 0
sumAll = 0

while i < 500000:
    for n in str(i):
        total = total + factorial(int(n))
    if total == i:
        sumAll = sumAll + total
    i+=1
    total=0
