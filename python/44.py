import math

def checkPent(n):
    soltn = (1 + math.sqrt(1+(12*(2*n))))/6
    if float(soltn).is_integer():
        return True
    else:
        return False

def Pent(n):
    return n*0.5*((3*n)-1)

i=1
limit = 10000
differences = []
pents= []

m=1
while m < 40:
    pents.append(Pent(m))
    m+=1

while i < limit:
    if checkPent((3*i)+1):
        differences.append((3*i)+1)
    else:
        differences.append(0)
    i+=1

a = 1
b = 0



while a < len(differences):
    while b < len(differences):
        if differences[a] != 0 and differences[b] != 0 and checkPent(differences[a] + differences[b]) and checkPent(abs(differences[b] - differences[a])):
            print(abs(differences[b] - differences[a]))
        b+=1
    b=0
    a+=1
