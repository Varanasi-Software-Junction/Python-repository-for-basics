n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        condition= row<=col
        if condition:
            print("0",end="")
        else:
            print("",end="")
        print()
