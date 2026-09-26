line=int(input("enter line number:"))
new_text=input("enter new text:")

with open("courses.txt","r") as file:
    content=file.readlines()
if 1 <= line <= len(content):
    content[line-1]=new_text
with open("courses.txt","w") as file2:
    file2.writelines(content)
