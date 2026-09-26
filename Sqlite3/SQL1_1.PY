import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()
cursor.execute("""
#create table students (
id integer,
name text,
age integer,
course text,
marks integer
)
""")
students = [
    (1, "Harika", 20, "Python", 85),
    (2, "Hema", 21, "Java", 72),
    (3, "Prasad", 20, "Python", 90),
    (4, "Ravi", 22, "SQL", 68),
    (5, "Sita", 21, "Python", 78)
]
