text = input("enter text:")
upper_count=0
lower_count=0
for x in text:
    if x.isupper():
        upper_count+=1
    elif x.islower():
        lower_count+=1   
print("upper count=",upper_count)
print("lower count=",lower_count)