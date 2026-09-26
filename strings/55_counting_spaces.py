text = input("enter text:")
count=0
for x in text:
    if x.isspace():
        count+=1
print("count=",count)