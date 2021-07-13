trains = {100:"rajdhani exp","stops":{1:{"station":"pt dindyal","distance":0},2:{"station":"ndls","distance":50},3:{"station":"grk","distance":80}}}
print(trains)
trainname = trains.get(100)
print(trainname)
stops=trains.get("stops")
print(stops)
for key in stops:
    print(stops.get(key))