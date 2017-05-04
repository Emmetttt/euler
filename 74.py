def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

repeat = []

def digitfac(n, a, count=1):
    global repeat
    s = 0
    for x in str(n):
        s = s + factorial(int(x))
    if s == a or s in repeat:
        repeat = []
        return count
    elif count > 60:
        return
    else:
        repeat.append(s)
        return digitfac(s, a, count+1)
    

i = 1
no = 0

while i < 1000000:
    if digitfac(i, i) == 60:
        no+=1
    i+=1
