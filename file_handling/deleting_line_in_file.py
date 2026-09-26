line=int(input("enter line:"))
with open("courses.txt","r") as file:
    content=file.readlines()
    
if 1 <= line <= len(content):
    del content[line-1] 

with open("courses.txt","w") as file2:
    file2.writelines(content)    