def colWidths(table):
    colWidths = [0] * len(table)
    count = 0
    for item in table:
        for i in range(len(item)):
            if len(item[i]) > colWidths[count]:
                colWidths[count] = len(item[i])
        count += 1
    return colWidths

def printTable(table, width):
    for j in range(len(table[0])) :
        for i in range(len(table)):
            print(table[i][j].rjust(width[i] + 1, ':'), end = '')
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana', 'mango'],
 ['Alice', 'Bob', 'Carol', 'David', 'Stefan'],
 ['dogs', 'cats', 'moose', 'goose', 'elephant']]

column_width = colWidths(tableData)
printTable(tableData, column_width)


