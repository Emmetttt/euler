max_fib = 4000000 ##terminates
fib = [1,2,3] ##first three given

for i in range(0,1000): ##arbitrary large range
    new_fib = fib[len(fib)-1] + fib[len(fib)-2]
    if new_fib < max_fib: ##if below the required 4 mill
        fib.append(new_fib)

sum_fib = 0

for i in fib:
    if i % 2 == 0: ##for even i
        sum_fib = sum_fib+i ##sums even i

print(sum_fib)
