######## CHAPTER 3 #########

#"def" name"(argument)" ":" "return" statement/value


# "None" represents the absence of a value


# Local ang Global scope


def spam() :
    eggs = 99
    bacon() # eggs variable from this function dies then bacon() function ends
    print(eggs)

def bacon() :
    ham = 101
    eggs = 0 #eggs variable exist only here


spam()

def shop() :
    global eggs #"Global" statement tells that the variable refers to global one
    eggs = 'shop'


eggs = 'global'
shop()
print(eggs)
