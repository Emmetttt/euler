total = 0

def product(a, b):
    return (a * b)
    
def sumation(x):
    global total
    y = x
    while y > 0:
        n=0
        while (x-n) > y:
            total = total + product((x-n),y)
            n+=1
        y-=1
    return total
            
v = 2*sumation(1000)
