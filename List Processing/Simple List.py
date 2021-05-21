l=[]
while True:
    print("0-Exit,1-Add,2-Remove,3-Change,4-print")
    n=int(input("Enter n"))
    if (n==0):
        break;
    if (n==1):
        print("Add")
        x=int(input("X="))
        l=l+[x]
        print(n)
    if (n==2):
        print("Remove")
        x=int(input("x="))
        l.remove(x)
        print(n)
    if (n==3):
        print("Change")
    if (n==4):
        print("print")
        print(l)