n=7
for row in reversed(range(1,n)):
    for left in range(1,row+1):
        print("0",end="")
    for space in range(1,2*n - 2*row):
        print(" ",end="")
    for left in range(1,row+1):
        print("0",end="")
    print()
for row in range(1,2*n):
    print("0",end="")