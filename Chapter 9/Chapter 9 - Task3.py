#! python3
# Filling in the Gaps - program finds all files with a given prefix
# e.x. spam001.txt, spam002.txt and locates any gaps in numeration.
# Then the program renames all the later files to close this gap.

import os, re, shutil, pprint

if not os.path.exists('C:\\Users\\arts\\Documents\\Python - LEARN\\Chapter 9 - Task3'):
    os.makedirs('C:\\Users\\arts\\Documents\\Python - LEARN\\Chapter 9 - Task3')
path = 'C:\\Users\\arts\\Documents\\Python - LEARN\\Chapter 9 - Task3'

fileRegex = re.compile(r'spam\d+.txt')
fileNameRegex = re.compile(r'spam([0]{,2})?')   # takes also 0s' as a part of the name - e.x. spam00 (spam001.txt)
fileNumRegex = re.compile(r'\d\d\d')            # takes only number  - e.x. 1 (spam001.txt)

files = []
for filename in os.listdir('.\\Chapter 9 - Task3'):
    if fileRegex.search(filename):              # checks if there is file with specific name's pattern - e.x. spam001.txt
        files.append(fileRegex.search(filename).group())    # collects name of file in list
files.sort()                                    # sorts the files (to be sure that spam001.txt is before spam002.txt)
pprint.pprint(files)                            # prints all matched files' name on the screen

mo = fileNumRegex.findall(str(files))           # collects all numbers of file - e.x. ['1', '2', ... ]
print('mo = '+ str(mo))
for i in range(len(mo)-1):
    if int(mo[i+1])-int(mo[i]) != 1:            # checks if there is gap between neighbouring numbers (files was sorted)
        print(str(os.path.join('.\\Chapter 9 - Task3',str(files[i+1])))+' '+ os.path.join('.\\Chapter 9 - Task3',(str(fileNameRegex.search(files[i]).group()+str(int(mo[i])+1))+'.txt')))
        shutil.move(os.path.join('.\\Chapter 9 - Task3',files[i+1]), os.path.join('.\\Chapter 9 - Task3',(str(fileNameRegex.search(files[i]).group()+str(int(mo[i])+1))+'.txt')))
        mo[i+1] = str(int(mo[i])+1)             # updates [i+1] item of list of files' number.

print('Done')


## TO DO make a program who makes gap to add in this place new file

def make_gap(files, mo):
    gapNum = int(input('Give a gap number...'))
    files.sort()
    for i in range(len(mo)-1,gapNum-1, -1):
        print(str(os.path.join('.\\Chapter 9 - Task3',str(files[i])))+' '+ os.path.join('.\\Chapter 9 - Task3',(str(fileNameRegex.search(files[i]).group()+str(int(mo[i])+1))+'.txt')))
        #shutil.move(os.path.join('.\\Chapter 9 - Task3',files[i]), os.path.join('.\\Chapter 9 - Task3',(str(fileNameRegex.search(files[i]).group()+str(int(mo[i])+1))+'.txt')))

#make_gap(files,mo)

changeFileRegex = re.compile(r'''
    #(?=[0][1-9]{2})
    ([0][0][1-9])
    #(?=[1-9]{3})
    ''', re.VERBOSE)
num = 10
text = 'spam009.txt'
podmiana = changeFileRegex.sub('%s' % (num), text)
print(podmiana)
    
    
    
    
