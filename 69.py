def tot(n):
    i = 2
    phi = 1
    while i < n-1:
        if n%i != 0:
            phi+=1
        i+=1
    return phi



i = 2
phi = 1
n=10
coprime = []

while i < n:
    if n%i != 0:
        print(i, n%i)
        phi+=1
        coprime.append(i)
    i+=1
    
