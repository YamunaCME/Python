num = int(input("Enter number: "))
temp=num
sum=1

for x in range(1,num+1):
    if(num % x == 0):
       sum=sum+x   
        
if(temp==sum):
   print(num,"is a perfect number") 
else:
    print(num,"is not a perfect number")    