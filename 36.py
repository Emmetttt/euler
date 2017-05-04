def convertBinary(n, binary):
    i = 0
    while n - 2**i > -1:
        i+=1
        
    if i > 0:
        n = n - 2**(i-1)
        binary = binary + 10**(i-1)
    else:
        n = n - 2**i
        binary = binary + 10**i

    if n > 0:
        return convertBinary(n, binary)
    else:
        return binary

def palindrome(x):
    individual = []
    backwards = ''
    for letter in str(x):
        backwards = letter + backwards
    if x == int(backwards):
        return True
    else:
        return False

i = 1
s = 0

while i < 1000000:
    if palindrome(i) == True and palindrome(convertBinary(i,0)) == True:
        s = s+i
        print(i, s)
    i+=1
