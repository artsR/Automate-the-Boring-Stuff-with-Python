#! python3
# countdown.py - Countdown program that plays an alarm at the end of the countdown


import time, subprocess

timeleft = 5
input('COUNTDOWN ! Press any key...')
timeStart = time.time()
while timeleft > 0:
    print(timeleft)
    time.sleep(1)
    timeleft -= 1
timeEnd = time.time()
subprocess.Popen(['start', 'kalimba.mp3'], shell=True)
print('Veryfication of countdown... No. of seconds passed: '
        + str(round(timeEnd - timeStart, 4)))
