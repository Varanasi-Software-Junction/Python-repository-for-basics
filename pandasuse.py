import pandas as pd
import xlrd
data=pd.read_csv("data.csv")
#print(data)
#print(type(data))
datadict=data.to_dict()
#print(datadict)
datarun=data["run"]
print(datarun)
print(datarun.median())
#print(data.run)
print(type(data.run))
datarun=data[data.run==23]
print(datarun)
datarun=data[data.name == "GH"]
print(datarun)
datarun=data[data.run== data.run.min()]
print(datarun)
print(data.describe())