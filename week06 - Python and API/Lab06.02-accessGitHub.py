import requests
import json

# api key will not work for me have tried all 3 that were given
apiKey = 'b55d312da577ba479f7dc4f8f3f5b1384bdf3b2e'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)