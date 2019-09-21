#! python3
#   - Text Files to Spreadsheet
# Reads in the contents of several text files and insert those contents into
# a spreadsheet, with one line of text row.
# The lines of the first text file will be in the cells of column A,
# the lines of the second text file in the cell of column B, and so on...

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
numFile = 0
## TODO utwórz petle która obroci sie 'numFiles' razy (dla kazdego pliku)
while True:
    filename = input('Input name of file to import (blank to exit)...')
    if filename == '':
        break
    numFile += 1
    textFile = open(filename)
    content = []
    content = textFile.readlines()
    textFile.close()
    # uzyj petli pobierajaca linie i jesli to mozliwe zapisujaca je od razu w excel
    for row in range(1, len(content)+1):
        ws.cell(row, numFile).value = content[row-1]
        
wb.save('Chapter 12 - TEXTtoEXCEL.xlsx')
print('Writing the Excel file finished.')
