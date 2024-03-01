import random as rd
import pandas as pd

numCols = 4
colNames = ['test', 'test2', 'test3', 'test4']
colTypes = ['Int', 'String', 'Boolean', 'Float']
colRange = [['0', '100'], ['rest', ' crest', ' fest'], ['True', 'False'], ['0', '2']]
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
            # index how many strings are in the list
            randVar = rd.randint(0, len(colRange[c]) - 1)
            colStr = colRange[c][randVar]
            rData.append(colStr)
        else:
            rData.append(rd.choice(('True', 'False')))
    colData.append(rData)
# print(colData)

# Turn lists into dictionary were the keys are the column names
dictData = {}
for name, data in zip(colNames, colData):
    dictData[name] = data

dataFrame = pd.DataFrame(dictData)
print(dataFrame)
