s1=set([1,3])
s2=set([2,3])
sub=s1-s2
print(sub)
s1.symmetric_difference_update(s2)
print(s1)
d={1:1,2:2}

d.update({1:"One",2:"Two"})
print(d)