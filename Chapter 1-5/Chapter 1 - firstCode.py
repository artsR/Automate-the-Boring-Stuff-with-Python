####### CHAPTER 1 #######


# this program exchange greetings

print ('I am Python. What is your name?') # say hello and ask about name
myName = input()

print ('Nice to meet you ' + myName )   #exchange greetings

print ('The length of you name is: ')
print (len(myName))
print ()
print ('What is your age?') #ask about age
myAge = input ()
print ('You will be ' + str(int(myAge) + 1) + ' in a year')


#check how "len()" function works
len('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
len('a')

# get familiar with some new functions which convert data type
## str()
## int()
## float()


# make some comparison between data
42 == '42'
42 == 42.0
42.0 == 0042.000

# more functions:
# https://docs.python.org/3/library/functions.html
