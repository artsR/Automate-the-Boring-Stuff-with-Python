########### CHAPTER 13 ###########


import PyPDF2
#(PdfFileReader & PdfFileWriter objects)

# Extracting text from PDF. Extracting Images/Charts/Media is impossible w/ this Module
    #it extracts text and returns it as a String
filename = 'Chapter 13.pdf'
pdfFileObj = open(filename, 'rb') # rb - read binary (word and pdf are binary files)
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0) # extracting page no. 1
print(pageObj.extractText())

pdfFileObj.close()

## If the PDF is encrypted:
pdfReader = PyPDF2.PdfFileReader(open('Chapter 13.pdf', 'rb'))
print(pdfReader.isEncrypted)
pdfReader.getPage(0) # I get error because password was not supplied

pdfReader.decrypt('rosebud') # delivering password... Returns '1' if passis ok
pageObj = pdfReader.getPage(0) # now I can see pages.


# Creating PDF
    # PyPDF2 cannot write arbitrary text to a PDF. Instead it is capable to
    #copy pages from other PDF, rotating pages, overlaying pages and encrypting.
'''
    1. Open one or more existing PDFs into PdfFileReader
    2. Create a new PdfFileWriter object
    3. Copy pages from PdfFileReader into PdfFileWriter object
    4. Use PdfFileWriter to write the output PDF
'''

## Copying Pages:
pdf1File = open('Chapter 13.pdf', 'rb')
pdf2File = open('Chapter 13_2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj) # add pages to the end of file

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj) # add pages to the end of file

pdfOutputFile = open('Chapter 13_combined.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

#pdf1File.close()
#pdf2File.close()

## Rotating Pages:
page = pdf2Reader.getPage(0)
page.rotateClockwise(90) # 90 or 180 or 270. I can use 'rotateCounterClockwise()
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('Chapter 13_rotated.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
pdf2File.close()

## Overlaying Pages: (adding a logo, timestamp or watermark to a page)
pageWatermark = pdf1Reader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
pageWatermark.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageWatermark)

for pageNum in range(1, pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
resultPdfFile = open('Chapter 13_watermarked.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
pdf1File.close()

## Encrypting PDf:
pdfFile = open('Chapter 13.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish', 'secretpasswd') # user passwd, owner passwd 
resultPdf = open('Chapter 13_encrypted.pdf', 'wb')
pdfWriter.write(resultPdf)

resultPdf.close()
pdfFile.close()
