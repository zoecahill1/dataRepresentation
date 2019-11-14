from github import Github
import requests

# personal 
# 2c9b7439c13cd1787826a685bc11a31e13164e0c

# remove the minus sign from the key
g = Github("2c9b7439c13cd1787826a685bc11a31e13164e0c")

 #for repo in g.get_user().get_repos():
 #    print(repo.name)
     #repo.edit(has_wiki=False)
     # to see all the available attributes and methods
     #print(dir(repo))


repo = g.get_repo("zoecahill1/PrivateRepo")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text

#print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
