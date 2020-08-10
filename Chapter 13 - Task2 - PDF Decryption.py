#! python3
# PDFdecryption.py - Find all pdf files in a given folder and its subfolders
#                   and decrypt the file if it is encrypted.
#                   If the password is incorrect, informs user and goes to next
#                   file.

import os, PyPDF2

password = input('Input password to decrypt PDFs...')

for folderName, subfolders, filenames in os.walk('.'):
    folder = os.path.abspath(folderName)
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(os.path.join(folder, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            print('Processing ' + filename +' ...', end='\t')
            if pdfReader.isEncrypted:
                try:
                    pdfReader.decrypt(password)
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for page in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(page))
                    outcomePDF = open(os.path.join(folder, 
                        os.path.splitext(filename)[0] + '_decrypted.pdf'), 'wb')
                    pdfWriter.write(outcomePDF)
                    pdfFile.close()
                    outcomePDF.close()
                    print('Decryption was successful.')
                except Exception as err:
                    print('Decryption  was unsuccessful. Error: %s' % (err))
            else:
                print('File wasn\'t decrypted.')
