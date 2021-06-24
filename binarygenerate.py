def printList(l,comb):
    rev=l
    #print(rev)
    n=len(rev)
    for i in range(n):
        if rev[i]==1:
            print(comb[i],",",end="")
    print()
l=[0,0,0]
comb=['A','B','C']
print(l)
n=len(l)
while True:
    found=False
    for i in range(n):
        if l[i]==1:
            l[i]=0

        else:
            found = True
            l[i]=1
            print(l)
            printList(l,comb)

            break

    if not found:
        break
print(l)

