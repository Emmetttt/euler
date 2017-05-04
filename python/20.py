def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

a = str(factorial(100))
i = 0
sum = 0

while i < len(a):
    sum = sum + int(a[i])
    i+=1

print(sum)
