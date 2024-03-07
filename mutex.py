from threading import Thread
from time import sleep
from random import random
from threading import Lock
def report(lock,id):
    with lock:
        print(f'thread {id} is done')

    
def task(lock,id,val):
    with lock:
        print(f'we are runniv {id} thread with slee {val}')
    sleep(val)
    report(lock,id)

lock=Lock()
for i in range(0,10):
    Thread(target=task,args=(lock,i,random())).start()



    

    