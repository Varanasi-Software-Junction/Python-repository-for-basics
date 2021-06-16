numberofrows=7
mid=(numberofrows + 1)/2
for row in range(1,numberofrows+1):
    for col in range(1,numberofrows + 1):
        condition=row+col==mid + 1 or row-col==mid-1 or col-row==mid-1 or row + col==numberofrows + mid
        if condition:
            print("0",end="")
        else:
            print(" ",end="")
    print()
