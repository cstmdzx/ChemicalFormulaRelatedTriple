import xlrd
import xlwt
from openpyxl import load_workbook

excelFromRDF = load_workbook('ChemicalRelated.xlsx')
excelFromConcept = load_workbook('EquationRelatedReactant.xlsx')

sheet1FromRDF = excelFromRDF['Sheet1']
sheet1FromConcept = excelFromConcept['Sheet1']
sheet2FromConcept = excelFromConcept['Sheet2']

rowsFromRDF = sheet1FromRDF.rows
rowsFromConcept = sheet1FromConcept.rows

setFromRDF = set()

for eachRow in rowsFromRDF:
    line = [col.value for col in eachRow]
    if line[0] not in setFromRDF:
        setFromRDF.add(line[0])
    else:
        continue

setUnfinished = set()
for eachRow in rowsFromConcept:
    line = [col.value for col in eachRow]
    if line[0] not in setFromRDF:
        setUnfinished.add(line[0])
    else:
        continue

# print sheetUnfinished
intLine = 0
# print sheetUnfinished.cell(1, 1).value
for eachItem in setUnfinished:
    # sheetUnfinished.put_cell(intLine, 0, 1, eachItem, 0)
    intLine += 1
    sheet2FromConcept.cell(row = intLine, column = 1, value = eachItem)
    # sheetUnfinished.put_cell(intLine, 0, 1, eachItem, 0)
    intLine += 1
    sheet2FromConcept.cell(row = intLine, column = 1, value = eachItem)

excelFromConcept.save('EquationRelatedReactant.xlsx')



