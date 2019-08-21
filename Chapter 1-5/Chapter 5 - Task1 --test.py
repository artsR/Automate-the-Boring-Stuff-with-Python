def countItems(items):
    count = {}
    for i in range(len(items)):
        count.setdefault(items[i], 0)
        count[items[i]] += 1
    return count


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']




def addToInventory(inventory, addedItems):

    for item in addedItems:
        #print('item ' + item)
        if inventory.get(item, 0):
           inventory[item] += addedItems[item]
          # print(inventory[item])
        else:
            inventory.setdefault(item, addedItems.get(item))
    return inventory 

inv = {'gold coin': 42, 'rope': 1}
print('Initial inventory: ' + str(inv))
print('I want to add: ' + str(countItems(dragonLoot)))
print('Modified inventory: ' + str(addToInventory(inv, countItems(dragonLoot))))


