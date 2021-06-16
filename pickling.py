import  pickle as p
file=open("h:/pickle/list.txt","wb")
p.dump([1,2,3],file)
file.flush()
file.close()
file=open("h:/pickle/list.txt","rb")
x=p.load(file)
print(x)