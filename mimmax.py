a,b,c=int(input()),int(input()),int(input())

max = a if a>b else b
print(max)
max= (a if a>=c else c) if a>=b else (b if b>=c else c)
print(max)
print(a if a>b else b)
#print(int(input("A=")) * int(input("B=")))
