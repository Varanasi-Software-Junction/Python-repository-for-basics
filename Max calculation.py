a=3
b=1
c=2

#Max of 2 numbers
if a>=b:
    max=a
else:
    max=b
print("Max=",max)


#Max of 3 numbers
if a>=b and a>=c:
    max=a
else:
    if b>=c:
        max=b
    else:
        max=c
print(max)
#Max of 3 numbers using elif
if a>=b and a>=c:
    max=a
elif b>=c:
    max=b
else:
    max=c
print(max)

#Max using or
if a<b or a<c:
    if b>=c:
        max=b
    else:
        max=c
else:
    max=a
print(max)

#Max using nested if else
if a>=b:
    if a>=c:
        max=a
    else:
        max=c

else:
    
    if b>=c:
        max=b
    else:
        max=c
print(max)


