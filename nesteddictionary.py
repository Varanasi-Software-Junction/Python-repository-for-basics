rahulresult={"phy":70,"math":60}
rahuldetails={"name":"Rahul","address":"LKO","result":rahulresult}
students={1: {"name":"Abhay","address":"Varanasi","result":{"phy":50,"math":60}},2:rahuldetails}
print(students)
while True:
    print("0-Exit, 1- Search by Roll No")
    option=int(input("Option \n"))
    if option==0:
        break
    if option==1:
        rollno=int(input("Roll No \n"))
        student=students.get(rollno)
        print(student)
        if student!=None:
            while True:
                print("0-Exit, 1-Name")
                option1=int(input("Option = \n"))
                if option1==0:
                    break
                if option1==1:
                    name=student.get("name")
                    print(name)

