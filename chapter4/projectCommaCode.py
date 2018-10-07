# project to add comma to list

spam = ['apples', 'bananas', 'tofu', 'cats']

def addComma(someList):
    someList = someList.insert(-1, 'and')


addComma(spam)

newList = spam

for commaSent in range(len(newList)-2):
    print(str(newList[commaSent]) + ', ', end='' ) 

print(str(newList[-2]) + ' ' + str(newList[-1]) ) 

