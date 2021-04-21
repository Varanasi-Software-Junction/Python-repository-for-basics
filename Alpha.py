n=4
a=ord("A")-1
for row in range(1,n+1):
    ch=chr(a+row)
    print(ch,end="")
for row in reversed(range(1, n )):
    ch = chr(a + row)
    print(ch, end="")
print()
for row in reversed(range(1,n)):
    for left in range(1,row+1):
        ch = chr(a + left)
        print(ch, end="")
    for space in range(1,2*n - 2*row):
        print(" ",end="")
    for left in reversed(range(1,row+1)):
        ch = chr(a + left)
        print(ch,end="")
    print()


for row in range(2,n):
    for left in range(1,row+1):
        print(ch,end="")
    for space in range(1,2*n - 2*row):
        print(" ",end="")
    for left in range(1,row+1):
        print(ch,end="")
    print()
for row in range(1,n+1):
    print(row,end="")
for row in reversed(range(1, n )):
     print(ch, end="")
print()





