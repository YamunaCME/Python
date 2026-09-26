class vehicle:
    def start(self):
        print("vehicles are started")
class car(vehicle):
       def start(self):
         print("car started")
class bike(car):
       def start(self):
         print("bike started")
c=car()
c.start() 