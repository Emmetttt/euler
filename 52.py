def digits(n):
    i = 0
    digits = []
    while i < len(str(n)):
        digits.append(str(n)[i])
        i+=1
    digits.sort()
    return digits

i = 1

while i < 10000000000:
    if digits(i) == digits(2*i) == digits(3*i) == digits(4*i) == digits(5*i) == digits(6*i):
        print(i)
        break
    i+=1
