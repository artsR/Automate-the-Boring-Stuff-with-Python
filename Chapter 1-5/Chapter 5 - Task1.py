def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for i, j in inventory.items():
        print(str(j) + ' ' + i)
        item_total += j
    print('Total number of items: ' + str(item_total))

def countItems(items):
    count = {}
    for i in range(len(items)):
        count.setdefault(items[i], 0)
        count[items[i]] += 1
    return count

def addToInventory(inventory, addedItems):

    for item in addedItems:
        #print('item ' + item)
        if inventory.get(item, 0):
           inventory[item] += addedItems[item]
          # print(inventory[item])
        else:
            inventory.setdefault(item, addedItems.get(item))
    return inventory



dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


while True:
    print('Add item to the list (leave blank to quit adding)')
    item = input()
    if item == '':
        break
    dragonLoot.append(item)



inv = {'gold coin': 42, 'rope': 1}
print('Initial inventory: ' + str(inv))
print('I want to add: ' + str(countItems(dragonLoot)))
#print('Modified inventory: ' + str(addToInventory(inv, countItems(dragonLoot))))
     

displayInventory(addToInventory(inv, countItems(dragonLoot)))




backpack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}





 
