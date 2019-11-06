import requests
import json


dataString = {'name':'newName'}

# api key will not work for me have tried all 3 that were given
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne/178735779'

response = requests.put(url, json=dataString, auth=('token',apiKey))

print(response.status_code)
print(response.text)