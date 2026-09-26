from threading import Thread
class EvenThread(Thread):
    def __init__(self,x):
     Thread.__init__(self)
     self.x=x
    def run(self):
        if x % 2 == 0:
            print(x,"even number")
class OddThread(Thread):
    def __init__(self,x):
      Thread.__init__(self)
      self.x=x
    def run(self):
        if x % 2 != 0:
            print(x," is odd number")

x=int(input("enter number:"))
t1=EvenThread(x)
t2=OddThread(x)
t1.start()
t2.start()            
        