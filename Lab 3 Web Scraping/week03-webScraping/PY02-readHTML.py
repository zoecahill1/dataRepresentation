from bs4 import BeautifulSoup

with open("../../Lab 2 Javascript/carViewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())