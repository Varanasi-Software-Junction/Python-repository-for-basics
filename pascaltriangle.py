def pascal(y,x):
    if x==1:
        return 1
    if x==y:
        return 1
    return pascal(y-1,x) + pascal(y-1,x-1)
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i + 1):
        print("{0} ".format(pascal(i,k))  ,end="")
    print()