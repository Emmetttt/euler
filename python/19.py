year = 1901
sundays = 0
day = 2 ##Starts on a tuesday #1=mon, 7=sun, 5=friday
month = 1 ##Starts on a january #1=jan, 12=dec

##months 1, 3, 5, 7, 8, 10, 12 have 31 days
##months 4, 6, 9, 11 have 30 days

m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while year < 2001:
    for x in m:
        day = day + x
        if day % 7 == 0:
            sundays+=1
    year+=1

print(sundays)
