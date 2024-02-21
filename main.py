# import pandas as pd

numColumns = 0
columnNames = []
columnTypes = []
numRows = 0
maxColumns = 10
maxRows = 200

#Random Generator - generates data to a .csv based on the amount of columns/rows, column names & types, you input

#Asking how many columns
print('How many columns you want? Max is ' + str(maxColumns))
numColumns = input()

while int(numColumns) > maxColumns:
    print('Went over maximum amount of columns. Please try again')
    numColumns = 0
    print('How many columns you want? Max is ' + str(maxColumns))
    numColumns = input()

print('How many rows you want to create? Max is ' + str(maxRows))
numRows = input()

#Asking how many rows
while int(numRows) > maxRows:
    print('Went over maximum amount of rows. Please try again')
    numRows = 0
    print('How many rows you want to create? Max is ' + str(maxRows))
    numRows = input()

#Naming each column and the type. For string types, make a list that the generator will use
columnsNd = 0
while columnsNd < int(numColumns):
    print('Name column ' + str(columnsNd + 1) + ':')
    colNamStr = input()
    columnNames.append(colNamStr)
    columnsNd = columnsNd + 1

    print('What TYPE is column ' + colNamStr + '? Float, Int, String, or Boolean')
    colTypStr = input()
    colTypStr = colTypStr.capitalize()
    while not (colTypStr == 'Float' or colTypStr == 'Int' or colTypStr == 'String' or colTypStr == 'Boolean'):
        print('Wrong TYPE. Please try again.')
        print('What TYPE is column ' + colNamStr + '? Float, Int, String, or Boolean')
        colTypStr = input()
        colTypStr = colTypStr.capitalize()

    columnTypes.append(colTypStr)
    # TEST
    print(columnsNd)
    print(columnNames)
    print(columnTypes)

#Random Generator

#Adding generator lists to a panda dataframe

#Export out as a .csv

#  TEST
# print(numColumns)
# print(numRows)