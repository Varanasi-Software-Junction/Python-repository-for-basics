import person as p
import currency as c
import bankaccount as b
p=p.Person("Sachin",22,"Mumbai")
print(p)
b=b.bankaccount(11,p,1000)
print(b)
b.deposit()
print(b)
b.withdrawl()
print(b)

