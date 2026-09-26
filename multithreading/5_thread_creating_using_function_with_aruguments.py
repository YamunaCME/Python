from threading import Thread
import time
def display(message,age):
 print(message,age)

t1=Thread(target=display,args=("yamuna","18"))
t1.start()

#addition of two numbers
def add(a,b):
    time.sleep(5)
    print("Sum:",a+b)

a=int(input("enter first value:"))
b=int(input("enter second value:"))

t2=Thread(target=add,args=(a,b))
t2.start()    