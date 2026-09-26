class A:
    def f1(self):
        print("f1") 
        
class B(A):
  def f2(self):
    print("---f2---")  
b=B()
b.f1()
b.f2()