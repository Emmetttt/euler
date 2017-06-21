def streak(n,i):
    if n%(i+1) != 0:
        return i
    return streak(n+1, i+1)

def P(s,N):
    i = 2
    output = 0
    while i < N:
        if streak(i,0) == s:
            output = output + 1
        i+=1
    return output

list_streaks = [0]*(4**31)

i=2
while i < 4**31:
    list_streaks[i-2] = streak(i,0)
    i+=1
