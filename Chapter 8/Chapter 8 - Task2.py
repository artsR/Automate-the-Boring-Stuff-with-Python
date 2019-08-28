#! python3
# The program let the user introduce his own words into the sentence in the file

import os, re

def check_catchwords(word):
    adjRegex = re.compile(r'ADJECTIVE(.)?')
    nounRegex = re.compile(r'NOUN(.)?')
    verbRegex = re.compile(r'VERB(.)?')

    if adjRegex.search(word):
        return 'adjective'
    elif nounRegex.search(word):
        return 'noun'
    elif verbRegex.search(word):
        return 'verb'
    else:
        return False 
    
new_file = open('fileTask2.txt', 'w')
new_file.write('''The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.''')
new_file.close()

catchwords = ['NOUN', 'VERB', 'ADJECTIVE']

new_file = open('fileTask2.txt', 'r')
fileContent = (new_file.read()).split()
new_file.close()
print(fileContent)

for i in range(len(fileContent)):
    print(fileContent[i])
    temp = check_catchwords(fileContent[i])
    if temp:
        print('Enter ' + temp + ':')
        changeRegex = re.compile(temp + '(.?)', re.I)
        print(changeRegex.search(fileContent[i]).group())
        text = input()
        mo = changeRegex.sub(r'%s\1' % text, fileContent[i])
        print(mo)
        fileContent[i] = mo

file = open('file_resultTask2.txt', 'w')
output = ' '.join(fileContent)
file.write(output)
file.close()

print(output)

        
