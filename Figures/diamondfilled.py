numberofrows=11
mid=(numberofrows + 1)/2
for row in range(1,numberofrows+1):
    for col in range(1,numberofrows + 1):
        condition=row+col>=mid + 1 and row + col<=numberofrows + mid and row-col<=mid-1 and col-row <=mid-1
        if condition:
            print("0",end="")
        else:
            print(" ",end="")
    print()
