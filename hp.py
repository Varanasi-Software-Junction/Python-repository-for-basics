product=1
x=2
n=7
seq=x
while n>0:
    if n % 2 != 0:
        product=product*seq
    n=n//2
    seq=seq*seq

print(product)