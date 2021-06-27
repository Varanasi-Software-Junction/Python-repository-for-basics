import pandas as pd
"""
Search by rollno
Search by name
Find topper in all subjects
Find failed students
Find passed students

"""
data = pd.read_csv("pandas.csv")
print(data)

name=data[data.name=="raj"]
print(name)
print("topper student")
toper=data[data.mark==154][data.rollno==2]
print(toper)


