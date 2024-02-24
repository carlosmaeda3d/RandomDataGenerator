# import pandas as pd

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
    colTypes.append(colTypStr)
    colRange.append(colRangeStr)

# TEST
print(columnsNd)
print(colNames)
print(colTypes)
print(colRange)

#Random Generator to make lists for each column

#Turning lists into a dictionary for pandas dataframe. Make column names keys

#Adding generator lists to a panda dataframe

#Export out as a .csv

#  TEST
# print(numColumns)
# print(numRows)