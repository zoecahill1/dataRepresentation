import requests
import json


dataString = {'name':'newName'}

# api key will not work for me
apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne/178735779'

response = requests.put(url, json=dataString, auth=('token',apiKey))

print(response.status_code)
print(response.text)