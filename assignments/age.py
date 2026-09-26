age = int(input("Enter age: "))

if  age <= 15 and age > 0:
   print("child")
elif age <= 20 and age > 15:
   print("teenger")
elif age <= 50 and age > 21:
   print("adult")
elif age <=100 and age>50: 
   print("senior citizion")
else:
   print("invalid input")