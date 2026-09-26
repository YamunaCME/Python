print("program start")
try:
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    z=x/y

except ZeroDivisionError as e:
    print("error",e)  
else:
    print(z)          
       