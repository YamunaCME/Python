class customer:
    def __init__(self,id,name,age):
     self.id = id
     self.name = name
     self.age = age

    def display(self):
      print(self.id,"",self.name,"",self.age)

e1 = customer(101,"hema",17)
e1.display()
e1 = customer(102,"yamuna",18)
e1.display()
e1 = customer(103,"sridevi",19)
e1.display()