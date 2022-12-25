import threading
import time

# function acting as a thread

stuff = []


def func(n):
    print("ran")
    for i in range(n):
        print(i)

    time.sleep(1)
    print("done")


# making a thread
# args=(4,) <= python specific syntax for tuples, has to have comma even if only one value
x = threading.Thread(target=func, args=(4,))

# program starts in one thread. #1 main thread
# this starts another thread. #2
x.start()

# thread synchronization
x.join()
print("active threads", threading.active_count())
