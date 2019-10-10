from bs4 import BeautifulSoup

with open("../../Lab 2 Javascript/carViewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#only gives first <tr>
#print(soup.tr)

# we want all <tr>
rows = soup.findAll("tr")
#loops until len of rows
for row in rows:
    #print(row)

    # for every row we look for the td contents
    cols = row.findAll("td")
    
    #define list to store text
    dataList = []

    #loops around each col and gives us the text contents
    for col in cols:
        #print(col.text)

        #altered so that data is saved in list rather than printed
        dataList.append(col.text)
    print(dataList)