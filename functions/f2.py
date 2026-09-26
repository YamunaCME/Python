#no arguments and no return type
def fun():
    print("abc")
fun()    

#with arguments and no return type
def fun(x):
    print(x)
fun(300) 
fun("hena")   

#no arguments and with return type

def fun():
    return 20+30
print("addition=",fun())

#with arguments and with return type
def fun(x,b):
  return x*b
print("multiplication=",fun(20,40))