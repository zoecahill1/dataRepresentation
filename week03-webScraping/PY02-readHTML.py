from bs4 import BeautifulSoup

with open("../week02-javascript/carViewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())