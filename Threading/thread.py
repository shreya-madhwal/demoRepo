from threading import Thread
import threading
from time import sleep
def func():
    print("hi in func")
    sleep(1)
    raise Exception("problem occured")

def custom_hook(args):
    print(f'thread fail:{args.exc_value}')

threading.excepthook(custom_hook)

thread=Thread(target=func)
thread.start()
thread.join()
print("back to main thread")


