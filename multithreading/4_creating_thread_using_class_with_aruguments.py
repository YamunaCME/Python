from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
      Thread.__init__(self)
      self.name=name

    def run(self):
        print("name=",self.name)
name=input("enter your name:")        
t1=MyThread(name)
t1.start()           