import math

def checkPent(n):
    soltn = (1 + math.sqrt(1+(12*(2*n))))/6
    if float(soltn).is_integer():
        return True
    else:
        return False

def checkTriag(n):
    soltn = (-1 + math.sqrt(1+(8*n)))/2
    if float(soltn).is_integer():
        return True
    else:
        return False

def Hex(n):
    return n*((2*n)-1)

def check(n):
    if checkTriag(Hex(n)) == checkPent(Hex(n)):
        return True
    else:
        return False

i = 144

while i < 100000:
    if check(i):
        Tnum = (-1 + math.sqrt(1+(8*Hex(i))))/2
        print(Tnum)
        i = 100000
    else:
        i+=1
