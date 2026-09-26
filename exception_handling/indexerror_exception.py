l1=[10,20,"abc",True]
try:
    ind=int(input("enter index value:"))
    print(l1[ind])
except IndexError as e:
    print("error",e)
except ValueError as i:
    print("invalid input ",i)    
