hour=int(input("enter a hour"))
minute=int(input("enter a minute"))
if hour<=11:
    hr=hour
    ampm="AM"
if hour==12:
    hr=hour
    ampm="PM"
if hour>12:
    ampm="PM"
    hr=hour-12
print(hr,minute,ampm,sep=".")



