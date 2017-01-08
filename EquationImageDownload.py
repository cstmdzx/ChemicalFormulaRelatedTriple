# -*-coding=utf-8-*-
import urllib
from PIL import Image
from openpyxl import load_workbook

excelChemistryKnowledgeBase = load_workbook('chemistryKnowledgebaseOutput.xlsx')

sheetKnowledgeTriple = excelChemistryKnowledgeBase['Sheet2']

rowsKnowledgeTriple = sheetKnowledgeTriple.rows

strPre = u'反应方程式'
intCount = 0
dictEquation = dict()

for eachRow in rowsKnowledgeTriple:
    line = [col.value for col in eachRow]
    # print line[0]
    if line[1] != strPre:
        continue
    else:
        # print line[0]
        if line[0] in dictEquation:
            continue
        # print type(line[2])
        if type(line[2]) != unicode:
            strUrl = ''
        else:
            strUrl = line[2]
        dictEquation[line[0]] = strUrl
        intCount += 1

'''
print intCount
for eachEquation in dictEquation:
    print eachEquation + ' ' + dictEquation[eachEquation]
'''

'''
for eachKey in dictEquation:
    print type(eachKey)
'''

while (True):
    strInput = raw_input('shuru: ')
    strInput = strInput.decode('utf-8')
    print type(strInput)
    print strInput
    if strInput in dictEquation:
        strUrl = dictEquation[strInput]
        # print strUrl
    else:
        continue
    strPath = 'temp.img'
    data = urllib.urlretrieve(strUrl, strPath)
    imgEquation = Image.open(strPath)
    imgEquation.show()



