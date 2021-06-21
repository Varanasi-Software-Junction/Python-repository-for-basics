from functools import cmp_to_key


def f(x):

    if (x % 2==0):
        return True
    else:
        return False
def f1(x,y):

    if (x>y):
        return True
    else:
        return False
def compare(x, y):
    return x - y
l=[1,2,3,4,5]
result=list(filter(f,l))
print(result)
result=list(filter(lambda x:x%2==0,l))
print(result)
add= lambda  x,y:x + y
print(add(1,2))
l=[(1,2),(3,-4)]
l.sort(key=lambda x:x[1])
print(l)
l=[3,2,55,6]
l.sort(key=cmp_to_key(compare))
print(l)

