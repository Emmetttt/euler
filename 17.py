OneToNine = [0,3,3,5,4,4,3,5,5,4]
TenToNineteen = [3,6,6,8,8,7,7,9,8,8]
TwentyToNinety = [0,6,6,6,5,5,7,6,6]
OnehundredToNinehundredand = [0,13,13,15,14,14,13,15,15,14]

Total100 = 0
Total = 0
i = 0 ##loop through one to nine
j = 0 ##loop through ten to nineteen
k = 0 ##loop through twenty to ninety
l = 0 ##loop through hundreds

while k < len(TwentyToNinety):
    while i < len(OneToNine):
        Total100 = Total100 + TwentyToNinety[k] + OneToNine[i]
        i+=1 
    i=0
    k+=1
while j < len(TenToNineteen):
    Total100 = Total100 + TenToNineteen[j]
    j+=1

while l < len(OnehundredToNinehundredand):
    Total = Total + (Total100 + (OnehundredToNinehundredand[l] * 99))
    l+=1

Total = Total + len("onethousand")
print(Total)
