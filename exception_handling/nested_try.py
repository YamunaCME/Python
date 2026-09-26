try:
    x=int(input("enter first number:"))
    try:
     y=int(input("enter second number:"))
     result=x/y
     print("result=",result)   
    except ZeroDivisionError as e:
      print("second number cannot be zero",e)
except ValueError as i:
    print("values must be numaric",i)  

          