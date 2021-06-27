import pandas as pd
data = pd.read_csv("pandas.csv")
print(data)
"""
datarun=data["run"]
print(datarun)

datarun=data.run
print(datarun)
max=datarun.max()
print(max)
print(datarun.median())
print(type(data))
print(data)
datanames=data["name"]
print(datanames)
print(type(datanames))
print(data.describe())
print(datanames.describe())

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
"""