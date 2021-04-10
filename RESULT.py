phy=int(input("enter a phy marks"))
chem=int(input("enter a chem marks"))
math=int(input("enter a math marks"))
if(phy>=40 and chem>=40 and math>=40) :
    print("pass")
    percent=(phy+chem+math)/3
    print(percent)
    if percent>=60:
        print("1st div")
    else:
        print("2nd div")
else:
    print("fail")
