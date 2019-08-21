####### CHAPTER 2 #########

# "False" = '' = 0 = 0.0
# "True" = everything what is not "False"

# "sys.exit()" closes the program


# "while" loop statement

## "while" condition ":"
###(1) "while True" "break" example
###(2) "while True" "continue" example

while True :
    print ('Who are you? ')
    name = input()
    if name != 'Artur' :
        continue  # return to evaluation while condition
    print('Hello Artur. What is the password, bro?')
    password = input()
    if password == 'sword' :
        break
print('Access Granted')


# "for" "in" "range()"

for i in range(5) :
    print(i)

total = 0
for i in range (101) :
    total = total + i
print(total)    # "print" function is outside of the loop

total = 0
for i in range (101) :
    total = total + i
    print(total)    # "print" function is contained in loop

for item in table:

for i, j in itemsDict.items():
    
## "range(x, y, step)" refers to initial and ending value of 'i'
    

# "continue" and "break" can be used.

