import person as p
class bankaccount:
    def __init__ (self,accountno,name,balance):
        self.accountno=accountno
        self.name=name
        self.balance=balance
    def deposit(self):
        amount=int(input("Enter a amount"))
        self.balance+=amount
    def withdrawl(self):
        amount=int(input("Enter a amount"))
        if(amount<=0 or amount>self.balance):
            print("invalid amount")
        else:
            self.balance-=amount
    def __str__(self):
        return"accountno={0},Acc Holder=[{1}],balance={2}".format(self.accountno,self.name,self.balance)




