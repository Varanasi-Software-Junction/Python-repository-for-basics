class Currency:
    def __init__(self,rupees,paisa):
        self.totalpaisa=100*rupees + paisa

    def __str__(self):
        sign = ""
        total=self.totalpaisa
        if self.totalpaisa<0:
            sign="-"
            total=-total
        rupees=total // 100
        paisa=total % 100


        if paisa<10:
            paisa="0{0}".format(paisa)
        if rupees < 10:
            rupees = "0{0}".format(rupees)
        return "{2}₹ {0}.{1}".format(rupees,paisa,sign)
    def __add__(self, other):
        c=Currency(0,self.totalpaisa + other.totalpaisa)
        return c
    def __sub__(self,other):
        c=Currency(0,self.totalpaisa-other.totalpaisa)
        return c
    def __mul__(self,other):
        c=Currency(0,self.totalpaisa*other.totalpaisa//100)
        return c
    def __divmod__(self, other):
        return Currency(0,0)
    def __ge__(self, other):
        return self.totalpaisa>=other.totalpaisa
    def __gt__(self,other):
        return self.totalpaisa>other.totalpaisa
    def __lt__(self,other):
        return self.totalpaisa<other.totalpaisa
    def __le__(self, other):
        return self.totalpaisa<=other.totalpaisa
c1=Currency(3,50)
print(c1)
c2=Currency(3,50)
print(c2)
sum = c1 + c2
print(sum)
print(c1-c2)
mul=c1*c2
print(mul)
print(c1>=c2)
print(c1>c2)
print(c1<c2)
print(c1<=c2)