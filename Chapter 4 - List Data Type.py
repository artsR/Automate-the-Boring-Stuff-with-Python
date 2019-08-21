######### CHAPTER 4 ##########


# [-1] - refers to the last index of a list
# [-2] - refers to the second last index of a list

# Augmented Assignment Operator
amount += 1  #it's the same expresion like "amount = amount + 1"
amount -= 1
amount *= 1
amount /= 1
amount %= 1

message = 'Hello'
message += ' world.' #as a result I get 'Hello world.'
message *= 3

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4] # lists elements 1:4 of a list
spam[1:3] # lists elements 2:3 of a list
spam[1:]  # lists all elements starting from second place (0 - indicates first element)
spam[:2]  # lists all elements up to 2 on a list


len(spam) # checking length of the list

[1, 2, 3] + ['A', 'B', 'C'] # combines two lists into one of length of 6 elements
['X', 'Y', 'Z'] * 3 # multiplays the list into list of 9 elements

box = ['car', 'bat', 'rat', 'lion']
del box [2] # deletes 'rat' and now 'lion' are moved up into box[2]

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):  # the way to extract values of a list.
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


'howdy' in ['hello', 'hi', 'howdy', 'heyas'] # return True or False value
'howdy' not in ['hello', 'hi', 'howdy', 'heyas'] # return True or False value


# Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size, color, dispotion = cat  # assignment subsequent items of list cat
                            # to respective variables
    #!! The number of variables and the length of the list must be exactly equal

#!! list variables don't contain lists - they contain references to lists.

# to copy list (not only its referance to address I may use:
import copy # contains both "copy()" and "deepcopy()" funtions
copy.copy(supplies)

copy.deepcopy() # it's going to copy also list which is included in the list.

