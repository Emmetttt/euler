check = [3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408]
it = [1.5]
numdem = [[3,2], [7,5]]
x = 2/5
xnd = [2,5]
i=0

while i < 1000:
    it.append(1+x)
    x = 1/(2+x)
    p = [xnd[1]*2, xnd[1]]
    xnd = [p[0]+xnd[0], p[1]]
    y = [xnd[0]*2, xnd[0]]
    numdem.append([y[1]+xnd[1], xnd[0]])
    xnd = [xnd[1], xnd[0]]
    i+=1

count = 0
j = 0

while j < len(numdem):
    if len(str(numdem[j][0])) > len(str(numdem[j][1])):
        count+=1
    j+=1
