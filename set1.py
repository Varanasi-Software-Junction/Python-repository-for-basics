c={"cricket","cricket,hockey","cricket,hockey,tennis","cricket,tennis"}
h={"cricket,hockey,tennis"}
t={"cricket,hockey,tennis","football"}
allsports=c.intersection(h).intersection(t)
print(allsports)
print(c.union(h).union(t))
print(c.difference(h))
print(t,c,t.difference(c))
n={"chess"}
h.update(n)
print(h)
h.add("basketball")
print(h)
s1=set([1,3])
s2=set([2,3])
print(s1,s2,s1.difference(s2))
x=s1.difference(s2)
print(x)
