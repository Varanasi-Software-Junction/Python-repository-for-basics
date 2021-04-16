n=7
for row in reversed( range(2,n+1)):
    for space in range(1,n-row +1):
        print(" ",end="")
    for col in range(1,2*row):
        print("0",end="")
    print()
for row in ( range(1,n+1)):
    for space in range(1,n-row +1):
        print(" ",end="")
    for col in range(1,2*row):
        print("0",end="")
    print()
