hour=int(input("enter a hour"))
minute=int(input("enter a minute"))
"""
11:45  11;45 AM
12:45   12:45 PM
13:45    1:45 PM   01:45 PM   12:05 PM

"""
x1="10"
x2="50"
x3= " AM"
if minute<10:
    x2="0" + str( minute)


print(x1,":",x2,x3)





