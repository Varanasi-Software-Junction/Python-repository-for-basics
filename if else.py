a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if a<b and a<c:
    min=a
elif b<c:
    min=b
else:
    min=c

if a>b and a>c:
    max=a
elif b>c:
    max=b
else:
    max=c
mid= a+b+c-min-max
print(min,max,mid)



