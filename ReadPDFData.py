import PyPDF2

pdfFile = open('C2E2-Guests-2018.pdf.coredownload.052146472.pdf','rb',)

pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFile.close()



