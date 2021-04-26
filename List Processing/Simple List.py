l1=[1,2,3,4]
l2=list(l1)
condition = l1 is l2
print(l1,l2)
print(condition)
#l1[0]=9
l1=l1+[9]
#l1.remove(3)
condition = l1 is l2
print(l1,l2)
print(condition)