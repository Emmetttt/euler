from decimal import * #increase precision
getcontext().prec = 1000

i = 2
maxplaces = 0

def recur(n):
    #d = Decimal(1) / Decimal(n)
    d = 1/n
    j = 9
    while len(str(j*d).split('.')[1]) > 1:
        j = int(str(j) + '9')
    j = j+1
    number = len(str(j).split('.')[0])-1
    return number   

while i < 1000:
    if recur(i) > maxplaces:
        maxplaces = i
        print(maxplaces)
    i+=1
