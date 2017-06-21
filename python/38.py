def pandig(n):
    concat = ''
    i=1
    while len(concat) < 8:
        concat = concat + str(n*i)
        i+=1
    output = int(concat)
    concat = [int(x) for x in concat]
    concat.sort()
    if concat == compare:
        return output
    else:
        return 0

n = 1
compare = [1,2,3,4,5,6,7,8,9]
maximum = 1

while n < 987654321:
    if pandig(n) > maximum:
        maximum = pandig(n)
    n+=1

print(maximum)
