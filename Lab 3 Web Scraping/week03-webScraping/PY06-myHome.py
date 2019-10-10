import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.myhome.ie/residential/galway/property-for-sale")

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHome.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


#print(soup.prettify())

#finds one listing
#listings = soup.find("div", class_="PropertyListingCard")
#print(listings)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []

    #finds one price
    price = listing.find(class_ = "PropertyListingCard__Price").text
    #print(price)
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    #print(entry)
    home_writer.writerow(entryList)
home_file.close()