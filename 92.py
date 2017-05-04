def adding(n):
    n = str(n)
    a = 0
    for x in n:
        a = a + int(x)**2
    return a

def chain(n):
    if adding(n) == 1:
        return 1
    elif adding(n) == 89:
        return 89
    else:
        return chain(adding(n))

i = 1
j = 0

while i < 10000000:
    if chain(i) == 89:
        j+=1
    i+=1
