# daemon thread = a thread that runs in the background , not important to run
#                 your program will not wait for daemon theads to complete before exiting
#                 non-daemon thread connot normally be killed , stay alive until task is complete

#                 ex. backgound tasks , garbage collection waiting for input , long running processing

import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print ("logged in for : "+ str(count) +"second")

x = threading.Thread(target=timer,daemon=True)
x.start()

x.setDaemon(True)
print(x.isDaemon)

answer = input("do you wish to exit?")