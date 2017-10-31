#! python3
# encryptPdfs.py

import os, sys, PyPDF2, shutil

# get the password with which to encrypt the pdf copies
password = sys.argv[1]

# walk through the folders and subfolders to find the PDF files
for folderName, subfolders, filenames in os.walk('.'):
    for subfolder in subfolders:
        for filename in filenames:
            if filename.endswith('.pdf'):

                # copy the pdf file and encrypt it
                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(password)
                newfilename = os.path.splitext(filename)[0] + '_encrypted.pdf'
                encryptedPdf = open(newfilename,'wb')
                pdfWriter.write(encryptedPdf)
                encryptedPdf.close()

                # check the copied file is actually encrypted
                newPdfFile = open(newfilename,'rb')
                newPdfReader = PyPDF2.PdfFileReader(newPdfFile)
                if newPdfReader.isEncrypted:
                    # if copy is encrypted delete the old file
                    if 0 != newPdfReader.decrypt(password):
                        os.unlink(filename)
                    
