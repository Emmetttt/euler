NN = 0
limit = 1000

for i in range(0, limit):
    if i % 3 == 0 or i % 5 == 0:
        NN = NN + i

print(NN)
