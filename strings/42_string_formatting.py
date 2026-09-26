#String formatting is used to insert values inside strings.
#Python supports:
#1. Concatenation
#2. % formatting
#3. format() method
#4. f-strings

#1.contatination:
name="yamuna"
course="python"
c=name+" is learning "+course
print(c)

#2.using % formatting
name="yamuna"
age=18
print("my name is %s and my age is %d" %(name,age))

#3.using formatmethod

#format() method
name="yamuna"
course="python"
c = "{} is learning {}".format(name,course)
print(c)

#indexed format()
name="yamuna"
course="python"
c = "{1} is learning {0}".format(name,course)
print(c)

#named format()
c = "{name} is learning {course}".format(
    name="yamuna",course="python")
print(c)

#4.using F-strings
name="yamuna"
course="python"
c = f" {name} is learning {course}"
print(c)

#expressions Inside F-Strings
a = 10
b = 20
print(f"Total = {a + b}")

#Formatting Decimal Values
price = 1234.56789
print(f"Price: {price:.2f}")
