num = int(input("enter number: "))
temp=num
sum=0

while num > 0:
    
    r=num%10
    sum=sum*10+r
    num=num//10

if temp==sum:
    print("given number is palindrome") 
else:
    print("not a palindrome")      