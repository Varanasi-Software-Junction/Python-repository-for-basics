r=2
p=250
r= r + p//100
p=p % 100
print("₹", r,p)

totalpaise=r*100 + p
r= totalpaise//100
p=totalpaise % 100
print("₹", r,p)
# 123     123 match boxes   12 X 10    3  12  1X10  1
#              123

# 2 rupees . 250 paise
# r=2, p=250  x1=p//100  , x2 p % 100
#      x1 = 25//100 =2           50