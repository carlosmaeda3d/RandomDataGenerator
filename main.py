import random as rd
import pandas as pd

numCols = 0
colNames = []
colTypes = []
colRange = []
numRows = 0
maxCols = 10
maxRows = 200

#Random Generator - generates data to a .csv based on the amount of columns/rows, column names & types, you input
#Asks how many columns
print('How many columns you want? Max is ' + str(maxCols))
numCols = input()

while int(numCols) > maxCols:
    print('Went over maximum amount of columns. Please try again')
    numCols = 0
    print('How many columns you want? Max is ' + str(maxCols))
    numCols = input()

print('How many rows you want to create? Max is ' + str(maxRows))
numRows = input()

#Asks how many rows
while int(numRows) > maxRows:
    print('Went over maximum amount of rows. Please try again')
    numRows = 0
    print('How many rows you want to create? Max is ' + str(maxRows))
    numRows = input()

#Naming each column, type, and range. For string types, make a list that the generator will use
columnsNd = 0
while columnsNd < int(numCols):
    print('Name column ' + str(columnsNd + 1) + ':')
    colNamStr = input()
    colNames.append(colNamStr)
    columnsNd = columnsNd + 1

    print('What TYPE is column ' + colNamStr + '? Float, Int, String, or Boolean')
    colTypStr = input()
    colTypStr = colTypStr.capitalize()
    while not (colTypStr == 'Float' or colTypStr == 'Int' or colTypStr == 'String' or colTypStr == 'Boolean'):
        print('Wrong TYPE. Please try again.')
        print('What TYPE is column ' + colNamStr + '? Float, Int, String, or Boolean')
        colTypStr = input()
        colTypStr = colTypStr.capitalize()
    if colTypStr == 'String':
        print('What are the strings for the column? Use a comma between each string.')
        colRangeStr = input()
        colRangeStr = colRangeStr.split(',')
    elif colTypStr == 'Boolean':
        print('Boolean chosen') #Delete this once corrected
        colRangeStr = ['True', 'False']
    else:
        print('What is the range? Example 0 - 100')
        colRangeStr = input()
        colRangeStr = colRangeStr.split('-')
    colTypes.append(colTypStr)
    colRange.append(colRangeStr)

#Random Generator to make lists for each column
colData = []

for c in range(int(numCols)):
    rData = []
    for r in range(int(numRows)):
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

#Turning lists into a dictionary for pandas dataframe. Make column names keys
dictData = {}
for name, data in zip(colNames, colData):
    dictData[name] = data

#Adding generator lists to a panda dataframe
dataFrame = pd.DataFrame(dictData)
print(dataFrame)

#Export out as a .csv