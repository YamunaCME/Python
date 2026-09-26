from abc import ABC,abstractmethod
class A(ABC):
    def f1(self):
        print("f1")

    @abstractmethod  
    def f2(self):
        pass
class B(A):
  def f2(self):
    print("---f2---")  
b=B()
b.f1()
b.f2()