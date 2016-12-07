import pdb

fileRDF = open('export (1).nt')
linesRDF = fileRDF.readlines()


fileChemicalReaction = open('ChemicalReaction', 'w')

n = 0



for eachlineRDF in linesRDF:
    eachlineRDF = eachlineRDF.replace('\n','')
    words = eachlineRDF.split(' ')
    if (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#ReactionEquation>') | (words[1] == '<http://edukb.org/knowledge/0.1/property/chemistry#IonicReactionEquation>'):
        print words[0]
        n += 1
    if words[1] == '<http://www.w3.org/2000/01/rdf-schema#label>':
        label = words[2]
        label = label.replace('"', '')
        print label
        print type(label)
        try:
            print label.decode('unicode-escape')
        except:
            continue
#print n
#print u'\u79bb\u5b50\u53cd\u5e94\u65b9\u7a0b\u5f0f'

