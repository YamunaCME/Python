class A:
    def __init__(self,x):
      self.x=x
  
class B(A):
    def __init__(self,x,y):
      super().__init__(x)  
      self.y = y

    def display(self):
        print(self.x+self.y)
b=B(10,20)
b.display()