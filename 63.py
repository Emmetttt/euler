i = 1
j = 1
count = 0

while j < 100:
    while len(str(j**i)) == i:
        count+=1
        i+=1
    i=1
    j+=1
