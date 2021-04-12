#For loops are run in Python using the range object
r=range(10)
print(r)
print(type(r))
"""
The range object contains three inputs
start, end and increment/decrement
end is required, start and incr/decr are optional. default value of start is 0
default value of incr/decr is 1
The range actually is from 0 to end-1
"""

r=range(5)#This will print from 0 to 4 increase by 1
print("range(5)")
for x in r:
    print(x)
r=range(2,5)#This will print from 2 to 4
print("range(2,5)")
for x in r:
    print(x)

r=range(2,10,3)#This will print from 2 to 9 incr by 3. 2,5,8
print("range(2,10,3)")
for x in r:
    print(x)

#Reverse loops This will simply reverese the range
r=range(2,10,3)#This will print from 2 to 9 incr by 3. 2,5,8
print("range(2,10,3)")
for x in r:
    print(x)
r=range(6)#This will print from 2 to 9 incr by 3. 2,5,8
r=reversed(r)
print("range(6)")
for x in r:
    print(x)

