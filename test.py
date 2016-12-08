# solve the unicode problem
# change it to chinese character

fileReaction = open('ChemicalReaction')
fileRes= open('ChemicalReactionChinese', 'wb')
raw = fileReaction.readlines()

lines = raw[0].split('\\n')

# print lines.__len__()
# print lines[0]
n = 0

for eachline in lines:
    n += 1
    words = eachline.split(' ')
    if words.__len__() < 3:
        continue
    # print lines.__len__()
    # print n
    # print words
    strSubject = words[0].decode('unicode-escape')
    strPredicate = words[1].decode('unicode-escape')
    strObject = words[2].decode('unicode-escape')
    fileRes.write(strSubject.encode('utf-8') + ' ')
    fileRes.write(strPredicate.encode('utf-8') + ' ')
    fileRes.write(strObject.encode('utf-8') + '\n')

fileRes.close()
fileReaction.close()

