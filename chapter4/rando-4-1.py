for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for s in range(len(supplies)):
    print('Index' + str(s) + ' in supplies is: ' + supplies[s])  

print('  ')

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print('Size of the cat is ' + size)
print('It has ' + color + ' color fur')

print('  ')

a , b = 'Alice', 'Bob'
print(a)
a, b = b, a
print(a)

print('  ')

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('howdy'))


print('  ')

import copy
spamm = ['A', 'B', 'C', 'D']
cheese = copy.copy(spamm)
cheese[1] = 42
print(spamm)
print(cheese)

spamm3 = spamm
spamm3[2] = 44
print(spamm)
print(spamm3)


list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)

