start = 999
palindrome = []
i = 0

while start > 900: ##assume largest palindrome is a product of 2 numbers above 900
    product = start * (start-i)
    if len(str(product)) == 6: ##only 6 digit can be palindrome
        if str(product)[0:3] == str(product)[5] + str(product)[4] + str(product)[3]:
            palindrome.append(product) ##adds the palindrome to the list
            i=0
            start = start-1 ##resets to initial conditions, first palindrome is largest
        i+=1
    else: ##if not 6 digit, new start
        start = start-1
        i=0

print(max(palindrome))
