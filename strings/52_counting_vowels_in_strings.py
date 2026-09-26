text = input("enter text:")
vowels="aeiou"
count1=0
count2=0
for x in text:
    if x in vowels:
        count1+=1
    else:
        count2+=1    
print("vowels count=",count1) 
print("consonants count=",count2)       
