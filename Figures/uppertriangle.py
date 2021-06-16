numberofrows=7
mid=(numberofrows + 1)/2
for row in range(1,numberofrows+1):
    for col in range(1,numberofrows + 1):
        condition=row + col<=2*mid
        if not condition:
            print("0",end="")
        else:
            print(" ",end="")
    print()
