############ CHAPTER 10 #############

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err: # if an Exception object is returned from boxPrint()
        # this except statement will store it in a variable named err.
        print('An exception happened: ' + str(err))

# raise Exception causes 'Traceback' information in console.
# The traceback is displayed by Python whenever a raised exception goes unhandled.

# traceback.format_exc() - the function is located in traceback Module
    # instead of crashing my program right when an exception occurs,
    # I can write the traceback information to a log file and
    # keep my program running.
import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# assertion
podBayDoorStatus = 'open'
# assert statement says: "I assert that this condition holds true,
# and if not, there is a bug somewhere in the program.
    # Unlike "exceptions", my code should not handle assert statement with
    # "try" and "except".
    # If an assert fails, program should crash fast to shorten the time between
    # the original cause of the bug and my first notice the bug.
    # Assertions are for programmer errors, not user errors.
    # For errors like 'file not was found..' or user enter invalid data
        # I have raising an exception.
    # Assertions are for development, not the final product. By the time I
        # hand off my program to someone else to run, it should be free of bugs
        # and not require the sanity checks.
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

market_2nd =    {'ns': 'green', 'ew': 'red'}
mission_16th =  {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)

    # Assertions can be disabled by passing the -0 option when running Python.

# Logging - describes when the program execution has reached the logging
    # function call and list any variables I have specified at that point in time
    # (sometimes I use print() to see what's going on in program. Logging
    # fills this role).
    # all "logging" in the code may be disabled by "logging.disable(loggin.CRITICAL)
#--- the program results are followed thanks to "logging"----------------------
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
## basicConfig() specifies what details about the LogRecord object I want to
        # see and how I want those details displayed.
logging.debug('Start of program')
## logging.debug() - prints log information
## debug() - call basicConfig()
## basicConfig() - specifies the format of information
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))

print(factorial(5))
logging.debug('End of program')
# write loggings to the file:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
    # format='%(asctime)s - %(levelname)s - %(message)s')
#------------------------------------------------------------------------------
# logging level of importance
'''
    DEBUG  logging.debug()
    The lowest level. Used for small details.
    Usually you care about these messages only when diagnosing problems.
    
    INFO   logging.info()
    Used to record information on general events
    in your program or confirm that things are working at their point in the
    program.
    
    WARNING logging.warning()
    Used to indicate a potential problem that
    doesn’t prevent the program from working but might do so in the future.
    
    ERROR logging.error() Used to record an error that caused the
    program to fail to do something.
    
    CRITICAL logging.critical() The highest level. Used to indicate a fatal
    error that has caused or is about to cause the program to stop running
    entirely.
                                                                             '''
