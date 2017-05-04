lex = ["1", "2", "3", "4"]
perms = []

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    
i = 0
j = 0
k = 0

while k < 4:
    fourth = lex[k]
    del lex[k]
    while j < 3:
        third = lex[j]
        del lex[j]
        while i < 2:
            x = fourth + third + lex[i] + lex[1-i]
            perms.append(x)
            i+=1
        lex.insert(j, third)
        j+=1
        i=0
    lex.insert(k, fourth)
    j=0
    k+=1
