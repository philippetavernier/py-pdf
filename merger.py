#from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2, os
pdfiles = []
for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
                if filename != 'merged.pdf':
                        pdfiles.append(filename)
                        
pdfiles.sort(key = str.lower)

pdfMerge = PyPDF2.PdfFileMerger()

for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfMerge.append(pdfReader)
pdfFile.close()
pdfMerge.write('merged.pdf')
