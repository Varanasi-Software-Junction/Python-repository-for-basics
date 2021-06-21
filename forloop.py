n=4
for i in range(1,2*n):
    print("0",end="")
print()
for i in range(1,n):
    for left in range(1,n-i+1):
        print("0",end="")
    for space in range(1,2*i):
        print(" ",end="")
    for right in range(1, n - i + 1):
        print("0", end="")
    print()