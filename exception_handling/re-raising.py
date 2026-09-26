try:
    x=int(input("enter integer value:"))

    if x < 0:
        raise ValueError("negitive values are not allowed")
except ValueError as e:
    print("error occur",e)
    raise     