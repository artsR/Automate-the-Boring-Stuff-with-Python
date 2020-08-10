#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
#                   a single pdf.

import os, PyPDF2

# Get all the PDF filename
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower) # case insensitive sorting

pdfWriter = PyPDF2.PdfFileWriter()
counter = 0
# Open each PDF
for pdf in pdfFiles:
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for page in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)

pdfOutput = open('Chapter 13_all.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


# Similar Programs:
## Cut out specific pages from PDFs.
## Reorder pages in a PDF.
## Create a PDF from only those pages that have some specific text,
    ##identified by 'extractText()'
