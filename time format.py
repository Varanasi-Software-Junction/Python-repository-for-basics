hour=int(input("enter a hour"))
minute=int(input("enter a minute"))
"""
11:45  11;45 AM
12:45   12:45 PM
13:45    1:45 PM   01:45 PM   12:05 PM

"""

if hour<=11:
    print(hour,":",minute," AM")
elif hour==12:
    print(hour, ":", minute, " PM")
else:
    print(hour-12, ":", minute, " AM")





