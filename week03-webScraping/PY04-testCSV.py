import csv

# creates new csv file in wait mode
employee_file = open('employee_file.csv', mode = 'w')
# makes writer - delimter is file seperator, quotechar tells it if your data has " in it not to read them as programming
employee_writer = csv.writer(employee_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

# add some data to file
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# should always close file when finished
employee_file.close()