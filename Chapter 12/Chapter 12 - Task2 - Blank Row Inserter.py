#! python3
# blankRowInserter.py - Takes 2 integer (N and M) and file name as argument.
#  Starting at raw 'N', it should insert 'M' blank rows into spreadsheet.

import os, sys, openpyxl

assert len(sys.argv) == 4, 'The number of argument was incorrect'

N = int(sys.argv[1])
M = int(sys.argv[2])
filename = os.path.join(os.getcwd(), sys.argv[3])

wb = openpyxl.load_workbook(filename)
ws = wb.active

wb_new = openpyxl.Workbook()
ws_new = wb_new.active

act = 0 # activator to put blank rows
for row in range(1, ws.max_row+1):
    if row == N:
        act = 1
    for cell in range(1, ws.max_column+1):
        ws_new.cell(row+M*act, cell).value = ws.cell(row, cell).value  


wb_new.save(os.path.join(os.getcwd(), 'Chapter 12 - BlankRowInserter.xlsx')
