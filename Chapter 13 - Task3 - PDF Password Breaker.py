#! python3
# PDFpasswordBreaker.py -

import PyPDF2

dictionaryFile = open('dictionary.txt', 'r')
words = dictionaryFile.readlines()

pdfFilename = input('Input PDF name...')
pdfFile = open(pdfFilename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

attr = 1
for word in words:
    if pdfReader.decrypt((word.strip('\n')).lower()):
        print('Good guess! The password is: ' + word.lower())
        attr = 0
        break
    elif pdfReader.decrypt((word.strip('\n')).upper()):
        print('Good guess! The password is: ' + word.upper())
        attr = 0
        break
if attr:       
    print('Unfortunately the password is not in the dictionary')
