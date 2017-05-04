##using euclids formula
##m>n>0

m = 2
n = 1
product = 0
x=True

while x == True:
    while n < 10000:
        while m < 10000:
            c = (m**2 + n**2)**0.5
            if c.is_integer():
                product = n + m + c
                if product == 1000:
                    abc = n*m*c
                    print(abc)
            m+=1
        n+=1
        m=n+1
    x=False
