d={}
while True:
    print("0-Exit,1-Add,2-Remove,3-Change,4-View,5-View All,6-Distance")
    n=int(input("Enter n"))
    if (n==0):
        break;
    if (n==1):
        print("Add Student")
        station=int(input("station = "))
        name=input("Name = ")
        d[rollno]=name

    if (n==2):
        print("Remove")
        rollno=int(input("Roll no = "))
        name=d.get(rollno)
        if name==None:
            print("Not found")
        else:
            print(name)
            d.pop(rollno)

    if (n==3):
        print("Change")
        rollno=int(input("Roll no = "))
        name=d.get(rollno)
        if name==None:
            print("Not found")
        else:
            name=input("Name = ")
            d[rollno]=name
    if (n==4):
        print("View")
        rollno=int(input("Roll no = "))
        name=d.get(rollno)
        print(name)
    if (n==5):
        print("View All")
        print(d)
