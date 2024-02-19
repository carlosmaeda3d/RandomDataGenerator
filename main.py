numColumns = 0
columnNames = []
columnTypes = []
numRows = 0
maxColumns = 10
maxRows = 200

print('How many columns you want? Max is ' + str(maxColumns))
numColumns = input()

while int(numColumns) > maxColumns:
    print('Went over maximum amount of columns. Please try again')
    numColumns = 0
    print('How many columns you want? Max is ' + str(maxColumns))
    numColumns = input()

print('How many rows you want to create? Max is ' + str(maxRows))
numRows = input()

while int(numRows) > maxRows:
    print('Went over maximum amount of rows. Please try again')
    numRows = 0
    print('How many rows you want to create? Max is ' + str(maxRows))
    numRows = input()

#  TEST
print(numColumns)
print(numRows)