# thread = a flow of execution . like a seprate order of instructions.
#                 however each thread takes a turn running to achieve concurrency
#                 GTL = (global iterpreter lock),
#                 allows only one threead to hold the cotrol of the python interpreter at any one time


# cpu bound = program / task spends most of its time waiting for internal events (cpu intensive)
#             use multiprocessing

# io bound = program / task spends most of its time waiting for external event (user input . web scraping)
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drank coffee")
def study():
    time.sleep(5)
    print("you finish studying")

x = threading.Thread(target=eat_breakfast,args=())
x.start()
y = threading.Thread(target=drink_coffee,args=())
y.start()
z = threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()


# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())