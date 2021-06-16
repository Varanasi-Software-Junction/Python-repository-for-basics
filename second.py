m=4
s=67
h=67
#print(int(2.499999999+0.5))
if(m<40 or s<40 or h<40):
    print("you are failed")
else:
    print("you are passed:")
    total = m+h+s
    percent=total/3
    percent=int(100*percent+0.5)/100
    print("Total={0}, Percent={1}".format(total,percent))
    division="Third"
    if(percent>=60):
        division="First"
    elif percent>=50:
        division="Second"
    print(division)
