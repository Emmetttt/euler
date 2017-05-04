target = 600851475143
divisor = 2

while target > divisor:
    if target % divisor == 0:
        target = target/divisor
        divisor = 2
    else:
        divisor = divisor + 1

print(divisor)
