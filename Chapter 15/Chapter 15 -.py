########### CHAPTER 15 #############


import time
#import cProfile #it's more detailed alternative for 'time' Module
#cProfile.run()        https://docs.python.org/3/library/profile.html


time.time() # how many seconds have passed from January 1, 1970

def calcProd():
    # Calculate the product of the first 100 000 numbers.
    product = 1
    for i in range(1, 1000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (round(endTime - startTime, 4)))

time.sleep(2) # stops program for 10 seconds


print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input() # press ENTER to begin
print('Started.')
startTime = time.time()
lastTime= startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')


# 'datetime' Module is useful to display a date in a more convenient format.
import datetime

datetime.datetime.now()
dt = datetime.datetime(2015, 10, 21, 18, 17, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

## To convert number of seconds from Unix Epoch to the date:
print(datetime.datetime.fromtimestamp(time.time()))#=datetime.datetime.now()

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)

print('halloween2015 == oct31_2015')
print(halloween2015 == oct31_2015)
print('halloween2015 > newyears2016')
print(halloween2015 > newyears2016)
print('newyears2016 != oct31_2015')
print(newyears2016 != oct31_2015)

## 'datetime' Module also provides a 'timedelta' data type = duration of time.
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print('delta.days, delta.seconds, delta.microseconds')#timedelta object has only
print(delta.days, delta.seconds, delta.microseconds)  #attributes: days,second and microseconds
print('delta.total_seconds()')
print(delta.total_seconds())
print(delta)
print(str(delta))

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1)
print(dt + thousandDays)

oct21st = datetime.datetime(2018,10,21,18,43,0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print('oct21st - aboutThirtyYears')
print(oct21st - aboutThirtyYears)
print('oct21st - (2 * aboutThirtyYears)')
print(oct21st - (2 * aboutThirtyYears))

''' the 'while' loop "pause" the program untill a certain date will be reached.

while datetime.datetime.now() < datetime.datetime(2019,2,1,18,0,0):
    time.sleep(1) # it will frozen program for second so the above condition
#                 will be checked once per second.
'''

## Converting 'datetime' Object into Strings - 'strftime()' Method:
'''
 strftime() Directives
 
    strftime            directive Meaning
    
        %Y          Year with century, as in '2014'
        %y          Year without century, '00' to '99' (1970 to 2069)
        %m          Month as a decimal number, '01' to '12'
        %B          Full month name, as in 'November'
        %b          Abbreviated month name, as in 'Nov'
        %d          Day of the month, '01' to '31'
        %j          Day of the year, '001' to '366'
        %w          Day of the week, '0' (Sunday) to '6' (Saturday)
        %A          Full weekday name, as in 'Monday'
        %a          Abbreviated weekday name, as in 'Mon'
        %H          Hour (24-hour clock), '00' to '23'
        %I          Hour (12-hour clock), '01' to '12'
        %M          Minute, '00' to '59'
        %S          Second, '00' to '59'
        %p          'AM' or 'PM'
        %%          Literal '%' character
                                                                        '''

print(oct21st.strftime('%Y/%m/%d %H:%M::%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

## Converting Strings into 'datetime' Object - 'strptime()' Method:
#       Using the same directives as 'strftime()'.
print(datetime.datetime.strptime('October 21, 2018', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 19:41:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))

