def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def x():
    return factorial(len(digits))/len(digits)

maxN = 9
nth = 1000000

digits = list(range(0,maxN+1))
i = 1
perm = []

while len(digits) > 0:
    while nth - i*x() > 0:
        i+=1
    nth = nth - (i-1)*x()
    if len(digits) > 1:
        perm.append(digits[i-1])
        del digits[i-1]
    else:
        perm.append(digits[0])
        del digits[0]
    i=1

lex = ""
for n in perm:
    lex = lex + str(n)

print(lex)
