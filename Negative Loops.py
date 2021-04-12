r=range(-5)
print(r)
print("range(-5)")
for i in r:#This loop will print nothing because start is 0 and is already greater than -5
    print(i)

r=range(-5,-1)#Start at -5 and go to -1. start = -5, end=-1, since loop goes to end-1, end-1 is -2
print("range(-5,-1)")
print(r)
for i in r:
    print(i)
r=range(-5,0)
print("range(-5,0)")
for i in r:
    print(i)

r=range(-1,-10,-1)
print(r)
print("range(-1,-10,-1)")
for i in r:
    print(i)
