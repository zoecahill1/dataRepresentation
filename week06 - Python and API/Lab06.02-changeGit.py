import requests
import json


dataString = {'name':'newName'}

apiKey = 'b4ddb9e5603da11cd857b83bad6ea6eb1819b92d'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne/178735779'

response = requests.put(url, json=dataString, auth=('token',apiKey))

print(response.status_code)
print(response.text)