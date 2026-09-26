line=int(input("enter line:"))
with open("courses.txt","r") as file:
    content=file.readlines()
if  1<= line <= len(content):
    print(content[line-1])
