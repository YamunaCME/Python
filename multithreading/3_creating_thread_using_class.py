from threading import Thread

class MyThread(Thread):
    def run(self):
        for x in range(10):
            print("thread=",x)

t1=MyThread()
t1.start()