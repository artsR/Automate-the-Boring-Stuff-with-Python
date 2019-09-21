#! python
# readCensusExcel.py - Counts both the total population and the number of census
# tracts for each county.

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {} # creating empty Dictionary variable

''' example of how 'countyData' variable will look like:

{'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
 'Aleutians West': {'pop': 5561, 'tracts': 2},
 'Anchorage': {'pop': 291826, 'tracts': 55},
 'Bethel': {'pop': 17013, 'tracts': 3},
 'Bristol Bay': {'pop': 997, 'tracts': 1},

e.x.     countyData['AK']['Bethel']['pop'] is equal to 17 013.
pattern: countyData[stateAbbv][county]['pop']
                                                                 '''
print('Reading rows...')
for row in range(2, sheet.get_highest_row()+1 ):
    #Each row in the spreadsheet has data for one census tract.
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value
   
    #Make sure the key for this state exists:
    countyData.setdefault(state, {})
                                # 'setdefault()' set a value if
                                # one does not already exist for state.
                                # 'countyData' needs dictionary as the value
                                # for each state abbrevation key,
    
    #Make sure the key for this county in this state exists:
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})
                                # each of those will need its own dictionary
                                # as the value for each county key.
                                # And each of those dictionaries will need
                                # keys 'tracts' and 'pop'

    # 'setdefault()' does nothing if the key already exists!                                

    #Each row represents one census tract, so increment by one:
    countyData[state][county]['tracts'] += 1
    #Increase the county 'pop' by the 'pop' in this census tract:
    countyData[state][county]['pop'] += int(pop)

#Open a new file and write the content of countyData:
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
        # 'pformat()' produces a string that is formatted as valid Python code.
        # So now I can import 'census2010.py' just like Module with created
        # data stracture 'countyData'.
resultFile.close()
print('Done.')


# Compare data across multiple rows in a spreadsheet.
# Open multiple Excel files and compare data between spreadsheets.
# Check whether a spreadsheet has blank rows or invalid data in any cells
    # and alert the user if it does.
# Read data from a spreadsheet and use it as the input for your Python programs.




    
