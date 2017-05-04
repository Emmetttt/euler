def powers(n):
    n = str(n)
    i=0
    k=0
    while i < len(n):
       k = k + int(n[i])**5
       i+=1
    if k == int(n):
        return True
    else:
        return False

i=2
fifth = []

while i < 999999:
    if powers(i) == True:
        fifth.append(i)
    i+=1
print(sum(fifth))
