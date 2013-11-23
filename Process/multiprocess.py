# Run two process simulatenously

# Tested on Python 2.7 (Ubuntu)

import multiprocessing
import time


def func1():

    print("In function 1")
    
    # Do some operations here
    time.sleep(4)

    print("Exiting Function 1")


def func2():
 
    print("In function 2")
    
    # Do some operations here
    time.sleep(5)
    print("Exiting function 2")


# Create a list of processes
Processes = []

# Start multiprocessing
for i in (func1,func2): 
    p = multiprocessing.Process(target=i,args=())
    p.daemon = True
    Processes.append(p)
    p.start()

# Wait for the processes to finish and join the Parent or current process.
for p in Processes:
    p.join()




