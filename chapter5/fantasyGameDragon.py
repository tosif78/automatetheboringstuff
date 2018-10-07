# fantasy video game

stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', 'diamond']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total = item_total + v
    print('Total number of items: ' + str(item_total)) 

def addToInventory(inventory, addedItems):
    for x in range(len(addedItems)):
        if addedItems[x] not in inventory.keys():
            inventory[addedItems[x]] =  1
        elif addedItems[x] in inventory.keys():
            inventory[addedItems[x]] =  ((inventory[addedItems[x]]) + 1)

#stuff = addToInventory(stuff, dragonLoot)  #messes it up.

addToInventory(stuff, dragonLoot)
displayInventory(stuff)
