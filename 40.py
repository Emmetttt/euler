champ = '0.'
i=1

while i < 1000001:
    champ = champ + str(i)
    i+=1

value = int(champ[2]) * int(champ[11]) * int(champ[101]) * int(champ[1001]) * int(champ[10001]) * int(champ[100001]) * int(champ[1000001])
