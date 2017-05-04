F = 0 ##Fn = x + y
Findex = 2
x = 1
y = 1

while len(str(F)) < 1000:
    F = x + y
    Findex += 1
    y = x
    x = F
