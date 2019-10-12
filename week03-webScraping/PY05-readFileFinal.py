from bs4 import BeautifulSoup
import csv

with open("../week02-javascript/carViewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")

for row in rows:

    cols = row.findAll("td")
    dataList = []
    for col in cols:
        dataList.append(col.text)

    # while loops test and remove update and deletes
    while ('Update' in dataList):
        dataList.remove('Update')

    while ('Delete' in dataList):
        dataList.remove('Delete')

    employee_writer.writerow(dataList)

employee_file.close()