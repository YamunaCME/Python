class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state

class Customer:
    def __init__(self,name,add):
        self.name=name
       

    def display(self,add):
        print(self.name)
        print(self.add.city,self.add.state)

a=Address("rajamundry","AP")
c= Customer("yamuna",)

c.display(a)           