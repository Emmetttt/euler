def addDigits(n):
    s=0
    for number in str(n):
       s = s + int(number)
    return s

i = 1
j = 1
largest = 0

while i < 100:
    while j < 100:
        if addDigits(i**j) > largest:
            largest = addDigits(i**j)
        j+=1
    i+=1
    j=1
