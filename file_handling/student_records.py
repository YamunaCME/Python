
with open("student.txt","a+") as file:
  stud_name=input("enter student name:")
  marks=input("enter marks:")
  course=input("enter branch:")
  record=f"{stud_name},{marks},{course} \n"
  file.write(record)
