#
# get text from clipboard, add star and space to beginning and paste into clipboard
#

import pyperclip

original = pyperclip.paste()
originalList = original.split('\n')
#print(originalList)

for x in range(len(originalList)):
    #print(f'* {originalList[x]}\n')
    originalList[x] = '* ' + originalList[x]

ouputList = '\n'.join(originalList)

pyperclip.copy(ouputList)


