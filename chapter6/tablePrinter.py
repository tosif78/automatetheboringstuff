#
# take list of strings
# display it in organized table, colums right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    # get max column length
    for x in range(len(tableData)):
        items = tableData[x]
        itemWidthMax = 0
        for y in range(len(items)):
            itemWidth = (len(items[y]))        
            if itemWidth > itemWidthMax:
                itemWidthMax = itemWidth
        colWidths[x] = itemWidthMax
    # loop to print table
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x]),end=' ')
        print('')

printTable(tableData)

