text = input("enter text:")
vowels="aeiou"
count=0
for x in text:
    if x not in vowels:
        count+=1
print("count=",count)  