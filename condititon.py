from threading import Condition
from threading import Thread
from time import sleep
con=Condition()
def task(con,listval):
    sleep(1)
    listval.append(30)
    print('notifying')
    with con:
        con.notify()

        

listval=list()
with con:
    thread=Thread(target=task,args=(con,listval))
    thread.start()
    con.wait()
print(f'got value {listval}')