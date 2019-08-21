######### CHAPTER 5 #########

# Methods
box = {'color': 'red', 'age': 42}

## keys() - returns keys as a tuples data type
for i in box.keys():
    print(i)
    
## values() - returns values as a tuples data type
for i in box.values():
    print(i)
    
## items() - returns items as a tuples data type
for i in box.items():
    print(i)

## get() - takes two argument: value to find, value to return if that key
        # does not exist
picnikItems = {'apples': 5, 'cups': 2}
print('Red Riding Hood is bringing ' + str(picnikItems.get('cups', 0)) + ' cups.')
print('Red Riding Hood is bringing ' + str(picnikItems.get('eggs', 0)) + ' eggs.')

## setdefault() - adding new element to the dic. in case it doesn't exist
import pprint

box.setdefault('name', 'Goblin')

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)



# simple example 

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham # the both dictonaries are equal despite the order of items is different


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True :
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')


# using multiple assignment trick in a for loop:
box2 = {'color': 'red', 'age': 42}
for i, j in box2.items():
    print('Key: ' + i + ' Value: ' + str(j))

