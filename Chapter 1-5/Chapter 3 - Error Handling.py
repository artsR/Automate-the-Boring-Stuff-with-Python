####### CHAPTER 3 #########


#Exception handling
## "try:" "except" statement

def spam(dividedBy) :
    try:
    return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(0))
print(spam(20))


try:
print(spam(2))
print(spam(0))  #causes error
print(spam(20)) #therefore this line will never execute because of "except"
except ZeroDivisionError:
    print('Error: Invalid argument')
