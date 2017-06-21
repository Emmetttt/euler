import numpy as np

primes = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
composite = [x for x in range(3,10000,2)]

produce = [1]

i = 0
while i < 999999:
    x = round(np.random.rand()*4)
    y = round(np.random.rand()*25)
    z = round(np.random.rand()*25)
    produce.append(primes[z] + (primes[y]+primes[x]**2))
    i+=1

produce.sort()

x = [x for x in np.array(composite) - np.array(produce)]

i = 0
while i < len(x):
    if x[i] == 0:
        del x[i]
    elif x[i] in primes:
        del x[i]
    elif x[i] % 2 == 0:
        del x[i]
    else:
        i+=1
