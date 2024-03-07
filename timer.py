from threading import Timer,Thread
def task(msg):
    print(f'{msg}')

thread=Thread(target=task,args=('hello'))
thread.start()
timer=Timer(3,task,args=("hello late"))
timer.start()