#! python3
# Excel2Text.py

import openpyxl, logging

def copyPoem(sheet,column,poemFileName):
    poemFile = open(poemFileName,'w')
    
    row = 1
    line = sheet[column+str(row)].value
    while line:
        logging.debug(str(row) + ': ' + line)
        poemFile.write(line)
        row = row + 1
        line = sheet[column+str(row)].value
        
    poemFile.close()

logging.basicConfig(level=logging.DEBUG, format=' %(message)s')
wb = openpyxl.load_workbook('poems.xlsx',read_only=True)
wks = wb.get_active_sheet()

copyPoem(wks,'A','poem1.txt')
copyPoem(wks,'B','poem2.txt')
copyPoem(wks,'C','poem3.txt')

wb.close()

