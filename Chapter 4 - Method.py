######## CHAPTER 4 ########

# methods don't return value, the execute some procedures.

# "index()" method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # the index of the value is returned. In this case: 0
                    # if the value isn't in the list, then "ValueError" produced


# "append()" and "insert()" methods
spam.append('moose') # adds new element to the list
spam.insert(1, 'chicken') # adds new element to the list in determined place



# "remove()" method
print(len(spam))
spam.remove('hi') # only first of reproduced 'hi' will be removed
print(len(spam)) # the length of the list will be shorter by removed items



# "sort()" method
chain = [2, 5, 3.14, 1, -7]
chain.sort() # this method sorts the list

words = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
words.sort() # it can also sort text list

chain.sort(reverse=True) # sorting in reverse order

## sort() method cannot be used for the list w/ different type of data
## sort() perceives order like this:  "Z" is before "a"

words.sort(key=str.lower) # treats all items in the list as lowercase
