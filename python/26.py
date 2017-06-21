def decimal(num, denom):
    x = 10
    a = True
    factor = 0
    while a == True:
        if x%denom == 0:
            factor = x/denom
            a = False
        else:
            x = x*10
        print(x/denom)
    return factor*num
