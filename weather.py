import  requests
import  json
url="http://api.openweathermap.org/data/2.5/weather?q=Varanasi&appid=4a1f8a61b74546825af1e0be106e797b"
response=requests.get(url)
print(response.status_code)
print(response.text)
jsondata=json.loads(response.text)
print(type(  jsondata))
print(jsondata["weather"][0]['description'])