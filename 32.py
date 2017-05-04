def digits(n):
    digits = []
    for a in str(n):
        digits.append(int(a))
    return digits

def length(a,b):
    return len(str(a) + str(b) + str(a*b))

pandigital = list(range(1,10))

a = 2
b = 1
product = 0
repeat = []

while len(str(a*b)) < len(pandigital)-2:
    while a < b:
        if length(a,b) == 9:
            x = digits(a) + digits(b) + digits(a*b)
            x.sort()
            if x == pandigital and a*b not in repeat:
                product = product + a*b
                repeat.append(a*b)
                print(product,a,b,a*b)
        a+=1
    b+=1
    a=1
