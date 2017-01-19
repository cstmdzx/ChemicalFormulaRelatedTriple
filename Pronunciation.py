from openpyxl import load_workbook

excelChemistryOutput = load_workbook('chemistryKnowledgebaseOutput.xlsx')
sheetKnowledgeBase = excelChemistryOutput['Sheet2']
rowsKnowledgeBase = sheetKnowledgeBase.rows

fileChemicalFormula = open('Formula', 'w')
fileUnannotatedFormula = open('UnannotatedFormula', 'w')

strUDZ = u'\u8bfb\u4f5c'
strUT = '\t'.decode()
strUN = '\n'.decode()

for eachRow in rowsKnowledgeBase:
    line = [col.value for col in eachRow]
    if line[1] == u'\u5316\u5b66\u5f0f':
        # print line
        if line[2] is None:
            fileUnannotatedFormula.write( (line[0] + strUN).encode('utf8') )
            continue
        strRes = line[2] + strUT + strUDZ + strUT + line[0] + strUN
        fileChemicalFormula.write(strRes.encode('utf8'))

fileChemicalFormula.close()
fileUnannotatedFormula.close()

