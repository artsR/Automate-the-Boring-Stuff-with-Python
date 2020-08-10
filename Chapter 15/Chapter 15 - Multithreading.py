########## CHAPTER 15 ############

import time, datetime

startTime = datetime.datetime(2029,10,31,0,0,0)
#while datetime.datetime.now() < startTime:
#    time.sleep(1)

print('Program now starting on Halloween 2029')


# Launching other app from level of python script:
import subprocess

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe.') # the function
#               returns the 'Popen' object which has 2 methods:
## 'poll()' - returns 'None' if process is still running
#                     '0'    if process was terminated correctly
#                     '1'    if process was terminated by error
## 'wait()' - it blocks program untill process has terminated. Returns '0' or '1'

print(calcProc.poll() == None)
print(calcProc.wait())
print(calcProc.poll())

subprocess.Popen(['C:\\Windows\\notepad.exe',
                  'C:\\Users\\arts\\Documents\\Python - LEARN\\guests.txt'])


# Some ideas for similar apps:
## Use 'time.sleep()' to give the user a chance to press CTRL-C to cancel an
#       action, such as deleting files. My program can print a
#       "Press CTRL-C to cancel" message and then handle any 'KeyboadInterrupt'
#       'exception' with 'try except' statements.
## For a long-term countdown, I can use 'timedelta' object to measure the number
#       of days, hours, minutes and seconds until some point (a birthday etc..)


