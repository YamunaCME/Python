from threading import Thread
import time
def display():
    for x in range(65,91):
     print(chr(x),end=" ")

t1=Thread(target=display())
t1.start()     