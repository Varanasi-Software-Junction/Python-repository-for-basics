rahulresult={"phy":70,"math":60}
rahuldetails={"name":"Rahul","address":"LKO","result":rahulresult}
students={1: {"name":"Abhay","address":"Varanasi","result":{"phy":50,"math":60}},2:rahuldetails}
print(students)
studentdetail=students.get(2)
if studentdetail==None:
    print("Not found")
else:
    print(studentdetail)
    address=studentdetail["address"]
    print("Address = ",address)
    result=studentdetail["result"]
    print(result)
    phy=result["phy"]
    print(phy)
