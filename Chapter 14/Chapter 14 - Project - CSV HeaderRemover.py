#! python3
# RemoveCSVheader.py - remove first row of the CSV file in the current working
#                   directory.

import os, csv

os.makedirs('Chapter 14 - CSV', exist_ok=True)

# Loop through every file in the current working directory
for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        continue
    print('Removing header from ' + filename + ' ...')

    # Read the CSV file in (skipping first row):
    csvRows = []
    csvFile = open(filename)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue # go to next circle of 'for' loop
        csvRows.append(row)
    csvFile.close()

    # Write out the new CSV file:
    outcomeCSV = open(os.path.join('headerRemoved', filename), 'w', newline='')
    csvWriter = csv.writer(outcomeCSV)
    for row in csvRows:
        csvWriter.writerow(row)
    outcomeCSV.close()

# Ideas for Similar Programs:
## Compare data between different rows in a CSV file or between multiple CSV files.
## Copy specific data from a CSV file to an Excel file, or vice versa.
## Check for invalid data or formatting mistaken in CSV files and alert the user
## Read data from a CSV file as input for my Python programs.
