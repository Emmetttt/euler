primes = [2,3,5,7] ##[2,3,5,7,11,13,17,19]
#numbers = [12,14,15,16,18,20]
numbers = [11,12,13,14,15,16,17,18,19,20]
#numbers = list(range(1,20))
#numbers = [6,7,8,9,10]
i = 20

def divisible(x):
    for number in numbers:
        k=0
        if x % number != 0:
            return False
        elif k==len(numbers):
            return True
        else:
            k+=1

while divisible(i) == False:
    i+=20
else:
    print(i)
