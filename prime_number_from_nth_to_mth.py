#print prime numbers from nth number to mth number
n = int(input('Enter the value of N: '))
m = int(input('Enter the value of M: '))
for i in range(n, m+1):
    for j in range(2, i//2+1):
        if i%j == 0:
            break
    else:
        print(i, end=" ")
