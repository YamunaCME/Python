student = {
    "name": "Yamuna",
    "age": 18
}

# Functions
print(student.keys())
print(student.values())
print(student.items())

student.update({"course": "CME"})
student.pop("age")

print(student)