import re
from openpyxl import load_workbook

excelEquationRelatedReactant = load_workbook('EquationRelatedReactant.xlsx')

sheetShengchengwu = excelEquationRelatedReactant['sheet_shengchengwu']

rowsShengchengwu = sheetShengchengwu.rows

fileRes = open('ProductTriple', 'w')
strUT = '\t'.decode()
strUN = '\n'.decode()
# print type(strUT)
strfyw = u'\u751f\u6210\u7269'

for eachRow in rowsShengchengwu:
    line = [col.value for col in eachRow]
    strEquation = line[0]
    lineValue = line[1:]

    for eachValue in lineValue:
        if eachValue is None:
            continue
        else:
            # print type(eachValue)
            strRes = (strEquation + strUT + strfyw + strUT + eachValue + strUN).encode('utf8')
            fileRes.write(strRes)

    # print line


