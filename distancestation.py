d={}
while True:
    print("0-Exit,1-Add,2-Remove,3-Change,4-View,5-View All,6-Distane")
    n=int(input("Enter n\n"))
    if(n==0):
        break
    if(n==1):
        print("Add")
        print("Enter station")
        station=input()
        distance=int(input())
        d[station]=distance
    if (n==2):
        print("Remove")
        print("Enter station")
        station=input()

        distance=d.get(station)
        if distance==None:
            print("Not found")
            continue
        del d[station]
        print("Removed")
    if  (n==3):
        print("Change")
        print("Enter station")
        station=input()
        distance=int(input())
        d[station]=distance
        distance=d.get(station)
        if name==None:
            print("Not found")
            continue
            distance=input("Enter distance\n")
            d[station]=distance
            print("Changed")
    if  (n==4):
        print("View")
        print("Enter station")
        station=input()
        distance=int(input())
        print(distance)
    if (n==5):
        print("View All")
    if (n==6):
        print("Distance")
    if n==7:

            for station in d:
                print("station=",station,"distance=,",d[station])
    if n==8:
            d.clear()