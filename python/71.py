import math
import operator

def hcf(n,d):
    i=1
    hcf = 1
    while i < n+1:
        if n % i == 0 and d % i == 0:
            hcf = i
        i+=1
    return hcf

d = 1000000
n = 1
l = []
a = {}

while d > 1:
    if hcf(n,d)==1:
        l.append([n,d])
        #a.update({"%d,%d" % (n,d):n/d})
        a.update({n/d:"%d,%d" % (n,d)})
    if n < d-1:
        n+=1
    else:
        d-=1
        n=1
        
