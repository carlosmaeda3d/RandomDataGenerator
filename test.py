import random as rd

numCols = 4
colNames = ['test', 'test2', 'test3', 'test4']
colTypes = ['Int', 'String', 'Boolean', 'Float']
colRange = [['0', '100'], ['rest', ' crest', ' fest'], ['True', 'False'], ['0', '1']]
numRows = 8
maxCols = 10
maxRows = 200

colData = []

for c in range(numCols):
    rData = []
    for r in range(numRows):
        if colTypes[c] == 'Int':
            randVar = rd.randint(int(colRange[c][0]), int(colRange[c][1]))
            # randVar = r + 1
            rData.append(randVar)
        elif colTypes[c] == 'Float':
            randVar = rd.uniform(float(colRange[c][0]), float(colRange[c][1]))
            # randVar = r + 1
            rData.append(randVar)
        elif colTypes[c] == 'String':
            # index how many string are in the list
            # colIndex = len(colRange[c]) - 1
            # randVar = rd.randint(0, colIndex)
            rData.append(rd.choice(('rest', ' crest', ' fest'))) # WORK ON
        else:
            rData.append(rd.choice(('True', 'False')))
    colData.append(rData)
print(colData)