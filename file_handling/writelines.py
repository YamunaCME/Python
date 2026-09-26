courses = [
    "python\n",
    "java\n",
    "c++\n"
]

with open("courses.txt","w+") as file:
    file.writelines(courses)
    file.seek(0)
    data=file.readline()
    print(data)
    print(file.tell())