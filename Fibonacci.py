a=0
"""
a=0
b=1
c=1
a=1
b=1
c=2
a=1
b=2
c=3
a=2
b=3
c=5
"""
b=1
n=100
print(1,"=",a)
print(2,"=",b)
for i in range(3,n+1):
    c=a+b
   # print(c / b)
    print(i,"=",c)
    a=b
    b=c