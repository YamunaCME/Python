class InvalidAgeError(Exception):
    def __init__(self,age,message="age must above 18"):
        self.age=age
        self.message=message
        super().__init__(self.message)
try:
    age=int(input("enter age:"))
    if age < 18:
        raise InvalidAgeError(age)
except InvalidAgeError as e:
    print("registration failed!",e)
else:
    print("registration completed sucessfully")                    
