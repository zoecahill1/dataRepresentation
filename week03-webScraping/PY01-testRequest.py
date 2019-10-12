import requests
from bs4 import BeautifulSoup

#use requests to get data
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-----------------")
# page.content is the div?
print(page.content)

# creates an instance of bs and calls the html parser
soup1 = BeautifulSoup(page.content, 'html.parser')
print("------------------")

# wraps text to make it nicely formatted
print(soup1.prettify())