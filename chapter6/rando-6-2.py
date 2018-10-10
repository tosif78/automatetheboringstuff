
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


for x in range(len(tableData)):
    items = tableData[x]
    print(items)
    itemWidthMax = 0
    for y in range(len(items)):
        itemWidth = (len(items[y]))        
        #print(itemWidth)
        if itemWidth > itemWidthMax:
            itemWidthMax = itemWidth
    print (itemWidthMax)  





colWidths = [0] * len(tableData)


#print(colWidths[0])
#print(colWidths[1])
