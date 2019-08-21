######### CHAPTER 6 #########

# \' single quote
# \" double quote
# \t tab
# \n new line
# \\ backslash

# r - I can use it before quote then I may put any character
print(r'That is /\ Carol\'s house')


print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# the same result I may get by formatting text like this:

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# Methods
spam = 'Hello world!'

## upper()
spam = spam.upper()
print(spam)
## lower()
spam.lower()
print(spam)
spam = spam.lower()
print(spam)
## isupper() - does the string has all letter are uppercase
## islower() - does the string has all letter are lowercase
## isalpha() - does the string consists only of letters
## isalnum() - does the string consists only of letters and numbers
## isdecimal() - does the string consists only of numeric characters
## isspace() - does the string consists only of spaces, tabs and new lines
## istitle() - does the string consists only of words that begins with uppercase

## startwith()
'Hello world!'.startswith('Hello')
## endswith()
'Hello world!'.endswith('Hello')

## join()- useful when I have a list of strings that need to be joined together
', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
## split()
'My name is Simon'.split() # by default is split wherever whitespace character are found
                            #(space, tab, newline) and they are excluded
'My!name!is!Simon'.split('!')
sentence = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
sentence.split('\n')

## rjust() - justify the text to the right 
'Hello'.rjust(10, '*') # justify to the rigth - all number of signs is 10
                        # '*' - putting '*' into free space
## ljust() - analogously like rjust but justify to the left.
## center() - like-for-like previouse two but centers the text.

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for i, j in itemsDict.items():
        print(i.ljust(leftWidth, '.') + str(j).rjust(rightWidth))

picnicItems = {'sandwiches' : 4, 'apples' : 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

## strip() - returns a new string without any whitespace characters
            # at the beginning or end. As an argument may pass character
            # which should be removed from the ends of the string
'    Hello World    '.strip()
'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS') == 'SpamSpamBaconSpamEggsSpamSpam'.strip('Spam') == 'SpamSpamBaconSpamEggsSpamSpam'.strip('mapS')
## lstrip() - removes whitespace from the left
## rstrip() - removes whitespace from the right

## pyperclip Module - Copying and Pasting strings from/to computer's clipboard
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
