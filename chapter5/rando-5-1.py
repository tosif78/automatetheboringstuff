
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')


spam = {12345: 'Luggage Combination', 42: 'The Answer'}

print(spam[42])

#
#
print('  ')
#
#

spamv = {'color': 'red', 'age': 42}
for v in spamv.values():
    print(v)
for k in spamv.keys():
    print(k)
for i in spamv.items():
    print(i)

#
#
print(' HERE ')
#
#

print(spamv.keys())
print(list(spamv.keys()))


#
#
print('  ')
#
#

spamvv = {'color': 'red', 'age': 42}
for k, v in spamvv.items():
    print('Key: ' + k + ' Value: ' + str(v))


#
#
print('  ')
#
#

spamin = {'name': 'Zophie', 'age': 7}
# 'name' in spamin.keys()
print('name' in spamin.keys())      #True
print('name' in spamin)             #True
print('color' in spamin)            #False
print('Zophie' in spamin.values())  #True
print('Zophie' in spamin)           #False

#
#
print('  ')
#
#

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')


#
#
print('  ')
#
#
