with open("courses.txt","r") as f1:
    content1=f1.read()
with open("student.txt","r") as f2:
    content2=f2.read()

with open("merged.text","w") as f3:
    f3.write(content1)
    f3.write(content2)
print("merging completed sucessfully!")                