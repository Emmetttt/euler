


def even(n):
    return n/2

def odd(n):
    return (3*n)+1

def collatz(k):
    count = 1
    while k > 1:
        if k % 2 == 0:
            k = even(k)
            count += 1
        elif k % 2 != 0:
            k = odd(k)
            count += 1
    return count

i = 13
longest = 0
colnumber = 0
counter = 1

while i < 1000000:
    k=i
    while k > 1:
        if k % 2 == 0:
            k = even(k)
            counter += 1
        elif k % 2 != 0:
            k = odd(k)
            counter += 1
    if counter > longest:
        longest = counter
        colnumber = i
    counter = 1
    i+=1

print(colnumber)
