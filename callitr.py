import  requests
import  json
url="http://itrplus.com/itr/api/sanctum/token?email=champaksworld@gmail.com&name=android&password=12345678"
data='{"email": "champaksworld@gmail.com","name":"Champak" "password": "toptal123", "password_confirmation": "toptal123"}'
response=requests.post(url,data)
print(response.status_code)
print(response.text)
