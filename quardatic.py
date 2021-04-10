a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b*b-4*a*c#16-4*1*2 16-8=8
print(d)
if (d>=0):
    d=d**.5
    r1=-(b+d)/(2*a)
    print(r1)
    r2 = -(b - d) / (2 * a)
    print(r2)