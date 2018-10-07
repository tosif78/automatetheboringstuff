# project to add comma to list

#spam = ['apples', 'bananas', 'tofu', 'cats']

userList=[]
while True:
    print('Enter item in your list')
    item = input()
    if item == '':
        break
    userList = userList + [item]  

def addComma(someList):
    for x in range(len(someList)-1):
        print(someList[x] + ',', end =" ")
    print('and ' + someList[-1] )

addComma(userList)


