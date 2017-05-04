words = open("words.txt", "r").read().split('","')
words[0] = words[0][1:]
words[-1] = words[-1][:-1]


alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
            'w': 23, 'x': 24, 'y': 25, 'z': 26}

def tnumber(n):
    return 0.5*(n*(n+1))

triangles = []
i=1

while i < 100:
    triangles.append(tnumber(i))
    i+=1

count = 0

for word in words:
    i = 0
    letterSum = 0
    while i < len(word):
        letter = word[i].lower()
        letterSum = letterSum + alphabet[letter]
        i+=1
    if letterSum in triangles:
        count+=1
    
