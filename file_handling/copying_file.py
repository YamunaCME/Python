with open("courses.txt","r") as  f1:
   with open("greeting.txt","w") as f2:
    for line in f1:
     f2.write(line)
print("file copied sucessfully!")    
        