i=2
j=2
terms = []

while i < 101:
    while j < 101:
        terms.append(i**j)
        j+=1
    i+=1
    j=2

print(len(set(terms)))

    
