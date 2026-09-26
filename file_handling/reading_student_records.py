with open("student.txt","r") as file:
    for record in file:
        stud_name,marks,course=record.strip()

        print("name:",stud_name)
        print("marks:",marks)
        print("branch:",course)
        print("--"*20)