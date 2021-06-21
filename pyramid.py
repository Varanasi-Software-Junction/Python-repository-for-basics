n=5
for row in range(1,n + 1):
    for space in range(1, n-row + 1):
        print(" ",end="")

    for o in range(1,row):
        print(o,end="")

        
    for o in reversed( range(1, row-1)):
        print(o, end="")
    print()