with open("courses.txt","r") as f:
    cont=f.read()
old=input("enter old content:") 
new=input("enter new content:")
updated_content = cont.replace(old,new)

with open("courses.txt","w") as f2:
    f2.write(updated_content)
print("text replaced sucessfully!")