i = 1
s = 0

while i < 1001:
    s = s + i**i
    i+=1

s=str(s)
print(s[-10:])
