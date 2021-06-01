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


c1=Currency(-10,50)
print(c1)
c2=Currency(11,50)
print(c2)
sum = c1 + c2
print(sum)
