#2000 Yes,  1900 No, 2020 Yes 2021 No
# If year is div by 400 it is leap year
# if year is div by 4 and not div by 100 leap year
# in all other cases not a leap year
year=int(input("Enter the year "))
if year % 400 ==0:
    print("Leap Year")
else:
    if year % 100 ==0:
        print("Not leap year")
    else:
        if year % 4==0:
            print("Leap Year")
        else:
            print("Not leap year")
