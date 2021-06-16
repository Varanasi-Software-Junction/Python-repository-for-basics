print("hello")
n=int(input("enter year"))
if(n%4==0) and(n%100!=0) or(n%400==0):
    print(n ,"is leap year")
else:
    print(n,"is not leap year")