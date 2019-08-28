#! python3
# Regex Search in files - program opens all .txt files in a folder and searches
# for any line that matches a user-supplied regular expression.
# The result is printed on the screen.

import os, re, pprint

# TO DO itroduction regular expression  by user
print('Introduce your regular expression, please:')
Regexexp = re.compile(input())
#Regexexp = re.compile(r'.*ala.*', re.DOTALL | re.I)
#print(Regexexp)

files = os.listdir('C:\\Users\\arts\\Documents\\Python - LEARN\\Chapter 8 - Task3')
print(files)

findings = []
for filename in files:
    file_work = open(os.path.join('.\\Chapter 8 - Task3', filename), 'r')
    file_content = file_work.readlines()
    file_work.close()
    for line in file_content:
        if Regexexp.search(line):
            findings.append(Regexexp.search(line).group())
pprint.pprint(findings)
