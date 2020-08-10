#! python3
# XLSXtoCSVconverter.py - Reads all the Excel files in folder and outputs them
#                   as CSV files. Each sheet in the file will be separeted CSV.
#                   Filename of the CSV should be <excel filename>_<sheet.title>.


import os, openpyxl, csv

folder = os.path.abspath('Chapter 14 - CSV')
print(folder)

for filename in os.listdir(folder):
    if filename.endswith('.xlsx'):
        wb = openpyxl.load_workbook(os.path.join(folder, filename))
        print('Reading ' + filename + '...')
        for sheet in wb.sheetnames:
            print(sheet, end='...')
            ws = wb[sheet]
            csvFile = open(os.path.join(folder, filename+'_'+sheet+'.csv'), 'w',
                           newline='')
            csvWriter = csv.writer(csvFile)
            for row in range(1, ws.max_row+1):
                rowData = []
                for cell in range(1, ws.max_column+1):
                    rowData.append(ws.cell(row, cell).value)
                csvWriter.writerow(rowData)
            print('  Sheet read correctly.')
        print('Creating CSV '+filename+' completed')
        csvFile.close()
