d={}
while True:
    print("0-Exit,1-Add,2-Remove,3-Change,4-View,5-View All,6-Distane,7-Seprate")
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
        print("Renove")
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
        distance=d.get(station)
        if distance!=None:
            print(distance)
        else:
            print("Enter distance")
            distance=int(input())
            d[station]=distance
    if (n==5):
            for station in d:
                print("station=",station,"distance=,",d[station])
    if (n==6):
        print("Distance")
    if  (n==7):
        print("Enter station1")
        station1=input()
        distance1=d.get(station1)
        print("Enter station 2")
        station2=input()
        distance2=d.get(station2)
        print(distance1-distance2)