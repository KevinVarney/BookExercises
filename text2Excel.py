#! python3
# text2Excel.py

import openpyxl, logging

def copyPoem(sheet,column,poemFileName):
    sheet.column_dimensions[column].width = 60
    poemFile = open(poemFileName)
    poem = poemFile.readlines()
    
    row = 1
    for line in poem:
        sheet.row_dimensions[row].height = 20
        sheet[column+str(row)] = line
        row = row + 1

logging.basicConfig(level=logging.DEBUG, format=' %(message)s')
wb = openpyxl.Workbook()
wks = wb.get_active_sheet()

copyPoem(wks,'A','poem1.txt')
copyPoem(wks,'B','poem2.txt')
copyPoem(wks,'C','poem3.txt')

wb.save('poems.xlsx')

