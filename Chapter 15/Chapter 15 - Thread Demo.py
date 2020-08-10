import threading, time

print('Start of program.')

def takeANap():
    #time.sleep(0.05)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

threadObj2 = threading.Thread(target=print, args=['Cats','Dogs','Frogs'],
                              kwargs={'sep':' & '})
threadObj2.start()
