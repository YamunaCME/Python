def f1(x,y):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("error",e)
        return None
           
a=int(input("enter first number:")) 
b=int(input("enter second number:"))
result=f1(a,b)
print("division of two numbers=",result)       
