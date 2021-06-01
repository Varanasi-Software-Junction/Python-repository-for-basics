class BankAccount:
    def __init__(self,accountno,name,balance):
        self.accountno=accountno
        self.name=name
        self.balance=balance
    def deposit(self):
        amount=int(input("amount=\n"))
        if(amount<=0):
            print("invalid amount")
        else:
            self.balance+=amount
    def withdrawl(self):
        amount=int(input("amount=\n"))
        if(amount<=0 or amount>self.balance):
            print("invalid amount")
        else:
            self.balance-=amount

    def __str__(self):
        return"AccNo={0},Name={1},Balance={2}".format(self.accountno,self.name,self.balance)
b1=BankAccount('11',"Pappu",1000)
b2=BankAccount('12',"Rahul",1000)
print(b1)
print(b2)
b1.deposit()
b2.deposit()
print(b1)
print(b2)
