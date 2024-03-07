from threading import Lock

lock = Lock()

def factorial(n):
    assert n > 0
    if n == 1:
        return 1
    
    with lock:       
        out = n * factorial(n - 1)

    return out
