import pdb

fileRDF = open('export (1).nt')
linesRDF = fileRDF.readlines()


fileChemicalReaction = open('ChemicalReaction', 'w')

n = 0

dictChemicalEquation = dict()  # map Uri to equation's text
setChemicalEquationUri = set()

for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n', '')
    words = eachlineRDF.split(' ')
    if (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#ReactionEquation>') | (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#IonicReactionEquation>'):  # recognize the NamedIndivadual of reaction equation
        if words[0] not in setChemicalEquationUri:  # add into the set
            # print words[0]
            n += 1
            setChemicalEquationUri.add(words[0])

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

for eachkey in dictChemicalEquation:
    print eachkey
    print dictChemicalEquation[eachkey]
print n

