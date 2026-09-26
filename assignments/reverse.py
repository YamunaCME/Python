num = int(input("enter number: "))
sum=0

while num > 0:
    
    r=num%10
    sum=sum*10+r
    num=num//10
print("reverse of a number:",sum)