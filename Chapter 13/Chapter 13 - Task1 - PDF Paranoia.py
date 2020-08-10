#! python3
# PDFparanoia.py - goes through every PDF in a folder (and subfolders) and
#               encrypt the PDFs with given password.
#               Each encrypted PDF should be saved with an '_encrypted.pdf' suffix.
#               Program attempts to read and decrypt the file to ensure that
#               it was encrypted correctly.
#               Program has also option to find all encrypted PDFs in a folder
#               and creates decrypted copy. If the password is incorrect
#               the message should be printed and it should continue to next file.

import os, sys, PyPDF2


# Set password:
if len(sys.argv) == 2:
    password = sys.argv[1]
else:
    password = input('Input password...')
    
# Go through all files in folder (and subfolders):
for folderName, subfolders, filenames in os.walk('.'):
    folder = os.path.abspath(folderName) #take absolute path of actual folder
    for filename in filenames:
        if filename.endswith('.pdf'):
            print(filename + ' processing...')
            pdfFile = open(os.path.join(folder, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            if pdfReader.isEncrypted:
                print('File already was encrypted.')
                pdfFile.close()
                continue
            # Copy PDF file and encrypt it:
            for page in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(page))
            try:
                pdfWriter.encrypt(password)
                print('Encrypted.')
            except:
                print('Impossible to encrypt ' + filename)
                pdfFile.close()

            # Create a name of file for encrypted version:
            outcomePDF = open(os.path.join(
                folder, os.path.splitext(filename)[0] + '_encrypted.pdf'), 'wb')
            pdfWriter.write(outcomePDF)
            pdfFile.close()
            outcomePDF.close()
            

#new_filename = re.compile(r'(.*).pdf).sub(r'\1, filename) + '_encrypted.pdf'

'''
while True
counter += 1
filename_counter exist?
continue
else:
filename += '_counter'
break
'''


