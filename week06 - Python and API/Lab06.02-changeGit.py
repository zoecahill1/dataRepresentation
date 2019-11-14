import requests
import json


dataString = {'private':'false'}

apiKey = '2c9b7439c13cd1787826a685bc11a31e13164e0c'
url = 'https://api.github.com/repos/zoecahill1/PrivateRepo/220297803'

response = requests.put(url, json=dataString, auth=('token',apiKey))

print(response.status_code)
print(response.text)

