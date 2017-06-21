num = 10
denom = 11

def frac(a, b):
    if a == b:
        return 0
    if a%10 == 0 or b%10 == 0:
        return 0
    a = [x for x in str(a)]
    b = [x for x in str(b)]

    aa = []
    bb = []
    for x in a:
        if x not in b:
            aa.append(x)

    for y in b:
        if y not in a:
            bb.append(y)

    if len(aa) == 2 or len(aa) == 0 or len(bb) == 0:
        return 0
    elif len(aa) != len(bb):
        return 0
    elif int(aa[0]) == 0 or int(bb[0]) == 0:
        return 0
    else:
        return int(aa[0])/int(bb[0])

finaldenom = 1
finalnum = 1

while num < 100:
    while denom < 100:
        if num/denom == frac(num, denom) and num/denom < 1:
            finaldenom = finaldenom*denom
            finalnum = finalnum*num
        denom+=1
    denom = 10
    num+=1

i=2
largest = 0
while i < finalnum+1:
    if finalnum%i == 0 and finaldenom%i == 0:
        print(i)
        largest = i
    i+=1
    

print(finaldenom/largest)
