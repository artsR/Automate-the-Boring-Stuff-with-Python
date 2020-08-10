############ CHAPTER 14 ############

import csv

csvFile = open('csv_example.csv')
csvReader = csv.reader(csvFile)#(1)'Reader' Object can be looped only once.
data = list(csvReader) # list of lists.
print(data[4][2])

csvFile = open('csv_example.csv')#(1)'Reader' was called before therefore
csvReader = csv.reader(csvFile)# I should re-read the csv file
                            # to not be empty in 'for' loop.

# Reading Data from Reader Objects in a 'for' loop:
    #it is useful for large files to avoid loading the entire file into memory
for row in csvReader:
    print('Row #' + str(csvReader.line_num) + ' ' + str(row))

# Writer Object:
outputCSV = open('output.tsv', 'w', newline='') # tsv - tab separated values
csvWriter = csv.writer(outputCSV, delimiter='\t', lineterminator='\n\n')
        # delimiter - what sign seperate elements in row (as default ',').
        # lineterminator - how the rows are seperated.
csvWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
csvWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
csvWriter.writerow([1, 2, 3.141592, 4])
outputCSV.close()
