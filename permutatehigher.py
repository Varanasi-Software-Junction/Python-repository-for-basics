number=41352
number=11121
number=12453
number=12345
ns=str(number)
print(ns)
l=[]
for ch in ns:
    l=l+ [ch]
n=len(l)
for i in range(n-1,1,-1):
    x1=l[i]
    x2=l[i-1]
    #print(x1,x2)
    if x2<x1:

        l[i]=x2
        l[i-1]=x1

        slice1=l[:i]
        slice2=l[i:]
        #print(slice1,slice2)
        slice2.sort()
        l=slice1 + slice2

        break
#print(l)
newnumber=""
for ch in l:
    newnumber=newnumber + ch
newnumber=int(newnumber)
print(newnumber)
