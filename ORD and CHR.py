n=4
for row in range(1,n+1):
    print(row,end="")
for row in reversed(range(1, n )):
     print(row, end="")
print()
for row in reversed(range(1,n)):
    for left in range(1,row+1):
        print(left,end="")
    for space in range(1,2*n - 2*row):
        print(" ",end="")
    for left in range(1,row+1):
        print(left,end="")
    print()






