########## CHAPTER 10 ############



# Debugger allows me to execute my program one line at a time

import random

heads = 0
for i in range(1, 1001):
    if random.randint(0,1) == 1:
        heads += 1
    if heads == 500:
        print('Halfway done! You\'ve met variance.') # set 'breakpoint' for debugger
print('Heads came up ' + str(heads) + ' times.')
