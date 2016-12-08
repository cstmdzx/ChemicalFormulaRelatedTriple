import pdb

fileRDF = open('export (1).nt')
linesRDF = fileRDF.readlines()


fileChemicalReaction = open('ChemicalReaction', 'w')

n = 0

dictChemicalEquation = dict()  # map Uri to equation's text
setChemicalEquationUri = set()

# search all equation's uri
for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#ReactionEquation>') | (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#IonicReactionEquation>'):  # recognize the NamedIndivadual of reaction equation
        if words[0] not in setChemicalEquationUri:  # add into the set
            # print words[0]
            n += 1
            setChemicalEquationUri.add(words[0])

# find all equation uri's label
for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if words[0] in setChemicalEquationUri:
        if words[1] == '<http://www.w3.org/2000/01/rdf-schema#label>':
            label = words[2]
            label = label.replace('"', '')
            # print label
            # print type(label)
            # try:
                # print label.decode('unicode-escape')
            # except:
                # continue
            dictChemicalEquation[words[0]] = label.decode('unicode-escape')

#print u'\u79bb\u5b50\u53cd\u5e94\u65b9\u7a0b\u5f0f'

'''
for eachkey in dictChemicalEquation:
    print eachkey
    print dictChemicalEquation[eachkey]
print n
'''

# find related Reactant's uri
setMaterialUri = set()  # save all related Uri
for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if words[0] in setChemicalEquationUri:
        if words[1] == '<http://edukb.org/knowledge/0.1/property/common#relatedTo>':
            if words[2] not in setMaterialUri:
                setMaterialUri.add(words[2])

'''
for eachkey in setMaterial:
    print eachkey

'''
m = 0
# find related uri's label
dictChemicalFormula = dict()
for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if words[0] in setMaterialUri:
        if words[1] == '<http://www.w3.org/2000/01/rdf-schema#label>':
            label = words[2].replace('"', '')
            label = label.decode('unicode-escape')
            dictChemicalFormula[words[0]] = label
            m += 1

'''
for eachkey in dictChemicalFormula:
    print eachkey
    print dictChemicalFormula[eachkey]
'''
# print m

listUriTuple = list()
for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if words[0] in setChemicalEquationUri:
        if words[1] == '<http://edukb.org/knowledge/0.1/property/common#relatedTo>':
            listUriTuple.append([words[0], '', words[2]])

listResTuple = list()
for eachTuple in listUriTuple:
    strSubject = dictChemicalEquation[eachTuple[0]]
    strPredicate = u'\u53cd\u5e94\u7269'
    if eachTuple[2] in dictChemicalFormula:
        strObject = dictChemicalFormula[eachTuple[2]]
    else:

        strObject = eachTuple[2].replace('\\\\', '\\')
        strObject = strObject.replace('"', '')
        strObject = strObject.decode('unicode-escape')
    listResTuple.append([strSubject, strPredicate, strObject])

intLen = listResTuple.__len__()

for eachTuple in listResTuple:
    print intLen
    print eachTuple[0] + ' ' + eachTuple[1] + ' ' + eachTuple[2]
    rin = raw_input('Choice(y/n)? ')
    intLen -= 1
    if rin == 'y':
        strTemp = eachTuple[0] + ' ' + eachTuple[1] + ' ' + eachTuple[2] + '\n'
        fileChemicalReaction.write(strTemp.encode('unicode-escape'))
    else:
        continue

