a=1
b=2
max = a if a>b else b
print(max)
c=3
max = a if a>c else c if a>b else b if b>c else c
print(max)