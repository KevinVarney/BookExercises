#! python3
# decryptPdfs.py

import os, sys, PyPDF2, shutil

# get the password with which to encrypt the pdf copies
password = sys.argv[1]

# walk through the folders and subfolders to find the PDF files
for folderName, subfolders, filenames in os.walk('.'):
    for subfolder in subfolders:
        for filename in filenames:
            if filename.endswith('_encrypted.pdf'):

                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)

                # decrypt the file
                if pdfReader.isEncrypted:
                    if 0 == pdfReader.decrypt(password):
                        print(password + 'is incorrect')
                    else:
                        # copy to a different file
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                        newfilename = filename.replace('_encrypted.pdf','.pdf')
                        decryptedPdf = open(newfilename,'wb')
                        pdfWriter.write(decryptedPdf)
                        decryptedPdf.close()

                    
