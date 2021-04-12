a=1
b=2
c=2
"""if a>=b:
    max=a
else:
    max=b
print(max)
"""
max = a if a>=b else b
print(max)

max = a if a>=c else c if a>=b else b if b>=c else c
print(max)
result= "Even" if a%2==0 else "Odd"
print(result)
print("Even" if int(input("Enter A ")) %2==0 else "Odd")


