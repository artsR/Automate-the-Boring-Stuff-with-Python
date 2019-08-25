######## CHAPTER 7 ##########

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))
#print('Okie dokie is a phone number:')
#print(isPhoneNumber('Okie dokie'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

''' It could be millions of characters long and the program would still run in
    less than a second. But using Regular Expresssions I can make it
    quicker to write a program.  '''

""" \d - any numeric digit from 0 to 9
    \D - any character that is not a numeric 0-9
    \w - any letter, numeric digit, or the underscore character (matchin "word" characters.)
    \W - any character that is not \w
    \s - any space, tab, newline character
    \S - any character that is not \s
    [0-5] = (0|1|2|3|4|5)                          """

# https://docs.python.org/3/library/re.html
# https://www.regular-expressions.info/


"""

    • The ? matches zero or one of the preceding group.
    • The * matches zero or more of the preceding group.
    • The + matches one or more of the preceding group.
    • The {n} matches exactly n of the preceding group.
    • The {n,} matches n or more of the preceding group.
    • The {,m} matches 0 to m of the preceding group.
    • The {n,m} matches at least n and at most m of the preceding group.
    • {n,m}? or *? or +? performs a nongreedy match of the preceding group.
    • ^spam means the string must begin with spam.
    • spam$ means the string must end with spam.
    • The . matches any character, except newline characters.
    • \d, \w, and \s match a digit, word, or space character, respectively.
    • \D, \W, and \S match anything except a digit, word, or space character,
    respectively.
    • [abc] matches any character between the brackets (such as a, b, or c).
    • [^abc] matches any character that isn’t between the brackets.


                                                                            """

import re  #contains regex functions

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('''12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'''))

# \d{3}  =   \d\d\d
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
myNumber = phoneNumRegex.search('My number is 415-555-1011')
print(myNumber.group())

# https://www.regexpal.com/

# adding "()" creates groups in the regex:
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
myNumber = phoneNumRegex.search('My number is 415-555-1011')
print(myNumber.group(2))
print(myNumber.groups())
areaCode, mainNumber = myNumber.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
myNumber = phoneNumRegex.search('My number is (415)-555-1011')
print(myNumber.group(1))
print(myNumber.group(2))

# pipe: | e.x. r'Batman|Tina Fey' - will match either Batman or Tina Fey.

## in this way I may find any of the strings: Batman','Batmobile', 
## 'Batcopter', and 'Batbat'
## they all have "Bat" prefix so the rest of the word may be choosen between
## elements included in "()"
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
result = batRegex.search('Batmobile lost a wheel')
print(result.group(1))


# I may want to find an optional group which doesn't have to appear in the text
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')

# "()*" - very similar use like "()?" but the optional item may appear
            # many times in the text
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batwowowowoman')
print(mo1.group())
mo2 = batRegex.search('The Adventure of Batwowowowowmawon') # error
    # because there is another 'wo' in different part than "()"

# "()+" the group has to appear at least once (obligatory) otherwise None returns
# "(){3}" obligatory to appear 3 times.
# "(){3,5}" obligatory to appear 3-5 times. Returns the longest possible!
# "(){3,5}?" obligatory to appear 3-5 times. Returns the shortest possible!
# "(){:5}" - max 5 times
# "(){3:} - min 3 times


# findall() method - returns all matched elements - not only first!
                # Returns "List" of strings (no groups in regular expression)
                # Returns "Tuples" (there are groups in regular expression)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Making my own character class.
vowelRegex = re.compile(r'[aeiouAEIOU]') # it returns all letter mentioned in the "()"
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
    # I may also use range of letters/numbers like: [a-zA-Z0-9]
    # r'[^aeiouAEIOU] - it is negative character class (everything except it)
    # r'^Hello' - means that expression has to be at the beginning of searched text
    # r'Hello$' - means that expression has to be at the end of searched text
    # "." - it matchs any character except for a newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
    # (.*) - matches everything except newline - it's greedy mode: tries to match
            # as much text as possible.
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
    # (.*?) - non-greedy mode.
nongreedyRegex = re.compile(r'<.*?>') # nongreedy way
greedyRegex = re.compile(r'<.*>')   # greedy way
nmo = nongreedyRegex.search('<To serve man> for dinner.>')
gmo = greedyRegex.search('<To serve man> for dinner.>')
print(nmo.group())
print(gmo.group())
    # re.compile('.*', re.DOTALL) it forces ".*" to match also newlines (all characters)
noNewLineRegex = re.compile('.*')
NewLineRegex = re.compile('.*', re.DOTALL)
print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
print()
print(NewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

    # re.compile(r'robocop', re.I) or re.IGNORECASE - to ignore upper or lower case

# Substituting Strings with "sub()" method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

    # using \1 or \2 ... etc. as argument of sub(). It returns only group 1 or 2 ...
agentNameRegex = re.compile(r'Agent (\w)\w*')
mo = agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)
    # re.VERBOSE as the second argument of re.compile()
        # the complicated regular expression:
#phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
        # I can simplify this using re.VERBOSE argument:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \s{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*zd{2,5})?    #extension
    )''', re.VERBOSE)
    # to combine re.VERBOSE, re.IGNORECASE and re.DOTALL I need to use "|"
someRegexValue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
    # second argument of re.compile:  https://nostarch.com/automatestuff/

