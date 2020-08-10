#! python3
# stopwatch.py


import time, pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit')
input() # press ENTER to begin
print('Started.')
startTime = time.time()
lastTime= startTime
lapNum = 1
results = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        first = '%s' % lapNum
        second = '%s' % totalTime
        third = '%s' % lapTime + ')'
        lap = 'Lap #' + (first+':' + (second + '(' + third.rjust(7)).rjust(15)).rjust(18)
        print(lap, end='')
        results.append(lap)
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying:
    print('\nDone.')
    pyperclip.copy('\n'.join(results))
