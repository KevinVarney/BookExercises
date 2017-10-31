#! python3
# getPassword.py

import docx, sys, PyPDF2

pdfFilename = sys.argv[1]
pdfFile = open(pdfFilename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
dictionary = open('dictionary.txt')
lines = dictionary.readlines()
dictionary.close()
firstLetter = 'Z'
for line in lines:
    if firstLetter != line[0]:
        firstLetter = line[0]
        print(firstLetter)
    word = line.rstrip()
    if pdfReader.decrypt(word) == 1:
        print ("password is " + word)
        break
    elif pdfReader.decrypt(word.lower()) == 1:
        print ("password is " + word.lower())
        break

        

    
